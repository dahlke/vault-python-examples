#!/bin/sh

export VAULT_ADDR="http://127.0.0.1:8200"
export VAULT_TOKEN="root"
export PG_HOST="127.0.0.1"

# echo "Enabling KV v2 secrets engine..."
vault secrets enable -path=secret -version=2 kv

echo "Writing the Example App and Admin KV policies..."
vault policy write vault-admin policies/admin-policy.hcl
vault policy write example-approle policies/example-approle-policy.hcl

echo "Seeding some sample secrets..."
vault kv put secret/applications/example-approle project_name="Super Addicting App Project X" lead_contact_email="neil@hashicorp.com"

echo "Enabling AppRole auth method..."
vault auth enable approle

echo "Configuring the AppRole auth method..."
vault write auth/approle/role/example-approle \
    secret_id_ttl=60m \
    token_num_uses=10 \
    token_ttl=60m \
    token_max_ttl=60m \
    secret_id_num_uses=40 \
	token_policies="example-approle"

echo "Configuring the PKI secrets engine..."

echo "Enabling the transit secrets engine..."
vault secrets enable transit

echo "Configuring the transit secrets engine..."
vault write -f transit/keys/example-transit-key

echo "Enabling the database secrets engine..."
vault secrets enable database

echo "Configuring the database secrets engine for Postgres for the root user..."
vault write database/config/example-postgresql-database \
    plugin_name=postgresql-database-plugin \
    allowed_roles="postgres-app" \
    connection_url="postgresql://{{username}}:{{password}}@$PG_HOST:5432?sslmode=disable" \
    username="postgres" \
    password="postgres"

echo "Configuring the database secrets engine for Postgres for the example AppRole role..."
vault write database/roles/postgres-app \
    db_name=example-postgresql-database \
    creation_statements="CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}'; \
        GRANT SELECT ON ALL TABLES IN SCHEMA public TO \"{{name}}\";" \
    default_ttl="30s" \

echo "Enabling the pki secrets engine..."
vault secrets enable pki

echo "Configuring the pki secrets engine..."
vault secrets tune -max-lease-ttl=8760h pki

echo "Update the CRL location and issuing certificates..."
vault write pki/config/urls \
    issuing_certificates="http://127.0.0.1:8200/v1/pki/ca" \
    crl_distribution_points="http://127.0.0.1:8200/v1/pki/crl"

echo "Configure a CA certificate and private key. Vault can accept an existing key pair, or it can generate its own self-signed root..."
vault write pki/root/generate/internal \
    common_name=example.com \
    ttl=8760h

echo "Configure a role that maps a name in Vault to a procedure for generating a certificate..."
vault write pki/roles/example-dot-com \
    allowed_domains=example.com \
    allow_subdomains=true \
    max_ttl=72h

echo "Done."
