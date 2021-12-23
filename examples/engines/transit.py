#!/bin/python3
# https://hvac.readthedocs.io/en/stable/usage/secrets_engines/transit.html

import base64
import hvac
import sys
import os

VAULT_ADDR = os.getenv("VAULT_ADDR")
VAULT_TOKEN = os.getenv("VAULT_TOKEN")

# NOTE: Vault currently defaults the `secret/` path to the KV secrets engine version 2 automatically
# when the Vault server is started in “dev” mode.

def base64ify(bytes_or_str):
    """Helper method to perform base64 encoding across Python 2.7 and Python 3.X"""

    if isinstance(bytes_or_str, str):
        input_bytes = bytes_or_str.encode('utf8')
    else:
        input_bytes = bytes_or_str

    output_bytes = base64.urlsafe_b64encode(input_bytes)
    return output_bytes.decode('ascii')


if __name__ == "__main__":
	client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)

	example_payload = "foobar"

	# Encrypt data
	encrypt_resp = client.secrets.transit.encrypt_data(name="example-transit-key", plaintext=base64ify(example_payload))
	ciphertext = encrypt_resp["data"]["ciphertext"]
	print("Encrypted data (ciphertext):", ciphertext)

	# Decrypt data
	decrypt_resp = client.secrets.transit.decrypt_data(name="example-transit-key", ciphertext=ciphertext)
	decrypted_plaintext_b64 = decrypt_resp["data"]["plaintext"]
	print("Decrypted ciphertext:", base64.urlsafe_b64decode(decrypted_plaintext_b64))
