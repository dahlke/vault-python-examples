#!/bin/sh

export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'

# echo "Enabling KV v2 secrets engine..."
# vault secrets enable -path=secret -version=2 kv

echo "Writing the Example App and Admin KV policies..."
vault policy write vault-admin policies/admin-policy.hcl
vault policy write example-app policies/example-app-policy.hcl

echo "Seeding some sample secrets..."
vault kv put secret/example-app project_name="Super Addicting App Project X" lead_contact_email="app-1@hashicorp.com"

echo "Enabling AppRole auth engine..."
vault auth enable approle

vault write auth/approle/role/example-app \
    secret_id_ttl=10m \
    token_num_uses=10 \
    token_ttl=20m \
    token_max_ttl=30m \
    secret_id_num_uses=40 \
	token_policies="example-app"

echo "Done."