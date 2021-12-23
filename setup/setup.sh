#!/bin/sh

export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'

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

echo "Configuring the transit secrets engine..."
vault secrets enable transit
vault write -f transit/keys/example-transit-key

echo "Configuring the database secrets engine..."

echo "Done."