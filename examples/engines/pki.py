#!/bin/python3
# https://hvac.readthedocs.io/en/stable/usage/secrets_engines/pki.html
from ssl import CertificateError
import hvac
import os

VAULT_ADDR = os.getenv("VAULT_ADDR")
VAULT_TOKEN = os.getenv("VAULT_TOKEN")


if __name__ == "__main__":
	client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)

	# Read CA certificate
	read_ca_certificate_response = client.secrets.pki.read_ca_certificate()
	print(f"Current PKI CA Certificate: {read_ca_certificate_response}")

	# Read CA certificate chain
	read_ca_certificate_chain_response = client.secrets.pki.read_ca_certificate_chain()
	print(f"Current PKI CA Certificate Chain: {read_ca_certificate_chain_response}")

	# Read certificate
	read_certificate_response = client.secrets.pki.read_certificate(serial="crl")
	print(f"Current PKI CRL: {read_certificate_response}")

	# List certificates
	list_certificate_response = client.secrets.pki.list_certificates()
	print(f"Current certificates (serial numbers): {list_certificate_response}")

	# Generate certificate
	generate_certificate_response = client.secrets.pki.generate_certificate(
		name="example-dot-com",
		common_name="demo.example.com"
	)
	print(f"Certificate: {generate_certificate_response}")

	# Revoke certificate
	revoke_certificate_response = client.secrets.pki.revoke_certificate(
		serial_number=generate_certificate_response["data"]["serial_number"]
	)
	print(f"Revoked Certificate: {revoke_certificate_response}")
