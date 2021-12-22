#!/bin/python3
# https://hvac.readthedocs.io/en/stable/usage/auth_methods/approle.html

import hvac
import os

VAULT_ADDR = os.getenv("VAULT_ADDR")
# VAULT_TOKEN = os.getenv("VAULT_TOKEN")
APPROLE_ROLE_ID = os.getenv("APPROLE_ROLE_ID")
APPROLE_SECRET_ID = os.getenv("APPROLE_SECRET_ID")

if __name__ == "__main__":
	# Purposely not passing in a token here to illustrated that we are not authenticated.
	client = hvac.Client(url=VAULT_ADDR, token="")
	print("is authenticated", client.is_authenticated())

	# List the secrets
	print("address", VAULT_ADDR, "role", APPROLE_ROLE_ID, "secret", APPROLE_SECRET_ID)

	client.auth.approle.login(
		role_id=APPROLE_ROLE_ID,
		secret_id=APPROLE_SECRET_ID,
	)

	print("TOKEN AFTER LOGIN", client.token)
	list_response = client.secrets.kv.v2.list_secrets(path="applications")
	print("LIST", list_response, "\n")

 	# Read the data written under path: secret/foo
	# Vault currently defaults the secret/ path to the KV secrets engine version 2 automatically when the Vault server is started in “dev” mode.
	read_response = client.secrets.kv.read_secret_version(path="applications/example-app")
	read_data = read_response["data"]["data"]
	project_name = read_data["project_name"]
	lead_contact_email = read_data["lead_contact_email"]
	print("Project Name:", project_name)
	print("Lead Contact Email:", lead_contact_email)

	# If you want to do the whole sequence through python.
	"""
	role_id_resp = client.auth.approle.read_role_id(
		role_name='some-role',
	)
	role_id =role_id_resp["data"]["role_id"]
	print(f'AppRole role ID for some-role: {role_id}')

	secret_id_resp = client.auth.approle.generate_secret_id(
		role_name='some-role',
		cidr_list=['127.0.0.1/32'],
	)
	secret_id = secret_id_resp["data"]["secret_id"]
	print(f'AppRole secret ID for some-role: {secret_id}')

	client.auth.approle.login(
		role_id=role_id,
		secret_id=secret_id,
	)
	"""