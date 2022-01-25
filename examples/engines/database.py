#!/bin/python3
# https://hvac.readthedocs.io/en/stable/usage/secrets_engines/database.html

import hvac
import os

VAULT_ADDR = os.getenv("VAULT_ADDR")
VAULT_TOKEN = os.getenv("VAULT_TOKEN")

ROLE_NAME = "postgres-app"

# NOTE: Vault currently defaults the `secret/` path to the KV secrets engine version 2 automatically
# when the Vault server is started in “dev” mode.

if __name__ == "__main__":
	client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)

	# List the connections
	list_connections_resp = client.secrets.database.list_connections()
	print("Current listed connections:", list_connections_resp)

	# Read the role
	read_role_resp = client.secrets.database.read_role(ROLE_NAME)
	print("Read role:", read_role_resp)

	# Generate a dynamic credential
	gen_cred_resp = client.secrets.database.generate_credentials(ROLE_NAME)
	print("Generated credentials:", gen_cred_resp)

