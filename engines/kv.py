#!/bin/python3
# TODO: https://hvac.readthedocs.io/en/stable/usage/auth_methods/approle.html

import hvac
import os

VAULT_ADDR = os.getenv("VAULT_ADDR")
VAULT_TOKEN = os.getenv("VAULT_TOKEN")

if __name__ == "__main__":
	# Purposely not passing in a token here to illustrated that we are not authenticated.
	client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)

	# List the secrets
	list_response = client.secrets.kv.v2.list_secrets(path="applications")
	print("LIST", list_response, "\n")

	# Read a secret
	read_response = client.secrets.kv.read_secret_version(path="applications/example-app")
	read_data = read_response["data"]["data"]
	project_name = read_data["project_name"]
	lead_contact_email = read_data["lead_contact_email"]
	print("Project Name:", project_name)
	print("Lead Contact Email:", lead_contact_email)

	# Update a secret

	# Create a new secret

	# Read the new secret

	# Update the new secret

	# Read the updated secret

	# Delete the updated secret

