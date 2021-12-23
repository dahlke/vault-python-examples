# vault-python-examples

Repo with Vault code samples using [`hvac`](https://hvac.readthedocs.io/en/stable).

## Setup

### Setup the `virtualenv` and install the depencencies

```bash
virtualenv venv
source venv/bin/activate
pip install -r pip-reqs.txt
```

### Start a Vault Dev Server

```bash
vault-ent server -dev -dev-root-token-id=root -log-level=debug
```

### Set up the Vault Server for the Examples

```bash
export VAULT_ADDR="http://127.0.0.1:8200"
export VAULT_TOKEN="root"
cd setup/
./setup.sh
```

## Auth Methods

### AppRole

```bash
unset VAULT_TOKEN
export APPROLE_ROLE_ID=$(vault read -format=json auth/approle/role/example-approle/role-id | jq -r .data.role_id)
export APPROLE_SECRET_ID=$(vault write -format=json -f auth/approle/role/example-approle/secret-id | jq -r .data.secret_id)
python auth/approle.py
```

## Secrets Engines

### KV

```bash
export VAULT_ADDR="http://127.0.0.1:8200"
export VAULT_TOKEN="root"
python engines/kv.py
```

### Transit

```bash
export VAULT_ADDR="http://127.0.0.1:8200"
export VAULT_TOKEN="root"
python engines/transit.py
```

### PKI

```bash
export VAULT_ADDR="http://127.0.0.1:8200"
export VAULT_TOKEN="root"
python engines/pki.py
```

### Databases

```bash
export VAULT_ADDR="http://127.0.0.1:8200"
export VAULT_TOKEN="root"
python engines/database.py
```
