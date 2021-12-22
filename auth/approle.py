#!/bin/python3
# https://hvac.readthedocs.io/en/stable/usage/auth_methods/approle.html

import hvac
import os

VAULT_ADDR = os.getenv("VAULT_ADDR")
# VAULT_TOKEN = os.getenv("VAULT_TOKEN")
APPROLE_ROLE_ID = os.getenv("APPROLE_ROLE_ID")
APPROLE_SECRET_ID = os.getenv("APPROLE_SECRET_ID")

def get_kv_secret_with_approle():
	# Purposely not passing in a token here to illustrated that we are not authenticated.
	client = hvac.Client(url=VAULT_ADDR, token="")
	print("is authenticated", client.is_authenticated())

	# Log into Vault
	client.auth.approle.login(
		role_id=APPROLE_ROLE_ID,
		secret_id=APPROLE_SECRET_ID,
	)

 	# Read the data written under path: secret/foo
	# Vault currently defaults the secret/ path to the KV secrets engine version 2 automatically when the Vault server is started in “dev” mode.
	read_response = client.secrets.kv.read_secret_version(path="applications/example-app")
	read_data = read_response["data"]["data"]
	project_name = read_data["project_name"]
	lead_contact_email = read_data["lead_contact_email"]
	print("Project Name:", project_name)
	print("Lead Contact Email:", lead_contact_email)

if __name__ == "__main__":
	get_kv_secret_with_approle()