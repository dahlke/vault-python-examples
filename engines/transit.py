#!/bin/python3
# https://hvac.readthedocs.io/en/stable/usage/secrets_engines/transit.html

import hvac
import os

VAULT_ADDR = os.getenv("VAULT_ADDR")
VAULT_TOKEN = os.getenv("VAULT_TOKEN")

# NOTE: Vault currently defaults the `secret/` path to the KV secrets engine version 2 automatically
# when the Vault server is started in “dev” mode.

if __name__ == "__main__":
	# Purposely not passing in a token here to illustrated that the client is not authenticated.
	client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)
