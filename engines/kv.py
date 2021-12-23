#!/bin/python3
# https://hvac.readthedocs.io/en/stable/usage/secrets_engines/kv_v2.html

import hvac
import os

VAULT_ADDR = os.getenv("VAULT_ADDR")
VAULT_TOKEN = os.getenv("VAULT_TOKEN")

# NOTE: Vault currently defaults the `secret/` path to the KV secrets engine version 2 automatically
# when the Vault server is started in “dev” mode.

if __name__ == "__main__":
	# Purposely not passing in a token here to illustrated that the client is not authenticated.
	client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)

	# List the secrets
	list_response = client.secrets.kv.v2.list_secrets(path="applications")
	print("Listed secrets:", list_response["data"])

	# Create a new secret
	client.secrets.kv.v2.create_or_update_secret(
		path="applications/example-kv",
		secret=dict(foo="bar"),
	)

	# List the paths again and see the one that was created
	list_response = client.secrets.kv.v2.list_secrets(path="applications")
	print("Listed secrets after creation:", list_response["data"])

	# Read the new secret
	# NOTE: TODO dev mode
	read_response = client.secrets.kv.read_secret_version(path="applications/example-kv")
	print("Created secret:", read_response["data"]["data"])

	# Update the new secret
	client.secrets.kv.v2.create_or_update_secret(
		path="applications/example-kv",
		secret=dict(foo="baz"),
	)

	# Read the updated secret
	read_response = client.secrets.kv.read_secret_version(path="applications/example-kv")
	print("Updated secret:", read_response["data"]["data"])

	# Delete the updated secret
	client.secrets.kv.v2.delete_metadata_and_all_versions(
		path="applications/example-kv",
	)
