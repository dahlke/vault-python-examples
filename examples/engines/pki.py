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
	read_ca_certificate_resp = client.secrets.pki.read_ca_certificate()
	print("Current PKI CA Certificate", read_ca_certificate_resp)

	# Read CA certificate chain
	read_ca_certificate_chain_resp = client.secrets.pki.read_ca_certificate_chain()
	print("Current PKI CA Certificate Chain:", read_ca_certificate_chain_resp)

	# Read certificate
	read_certificate_resp = client.secrets.pki.read_certificate(serial="crl")
	print("Current PKI CRL:", read_certificate_resp)

	# List certificates
	list_certificate_resp = client.secrets.pki.list_certificates()
	print("Current certificates (serial numbers):", list_certificate_resp)

	# Generate certificate
	generate_certificate_resp = client.secrets.pki.generate_certificate(
		name="example-dot-com",
		common_name="demo.example.com"
	)
	print("Certificate:", generate_certificate_resp)

	# Revoke certificate
	revoke_certificate_resp = client.secrets.pki.revoke_certificate(
		serial_number=generate_certificate_resp["data"]["serial_number"]
	)
	print("Revoked Certificate:", revoke_certificate_resp)
