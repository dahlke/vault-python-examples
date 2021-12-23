# vault-python-examples

Repo with Vault code samples using [`hvac`](https://hvac.readthedocs.io/en/stable).

## Setup

### Set up the `virtualenv` and install the depencencies

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

### Set up a Local Postgres Container

Start a `postgres` containe.

```bash
export PGPASSWORD=postgres
docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=$PGPASSWORD -d postgres
```

Once it's started, you can confirm you can connect with the Postgres client.

```bash
psql -U postgres -h localhost -p 5432
```

## Auth Methods

### AppRole

```bash
unset VAULT_TOKEN
export APPROLE_ROLE_ID=$(vault read -format=json auth/approle/role/example-approle/role-id | jq -r .data.role_id)
export APPROLE_SECRET_ID=$(vault write -format=json -f auth/approle/role/example-approle/secret-id | jq -r .data.secret_id)
python examples/auth/approle.py
```

## Secrets Engines

### KV

```bash
export VAULT_ADDR="http://127.0.0.1:8200"
export VAULT_TOKEN="root"
python examples/engines/kv.py
```

### Transit

```bash
export VAULT_ADDR="http://127.0.0.1:8200"
export VAULT_TOKEN="root"
python examples/engines/transit.py
```

### PKI

```bash
export VAULT_ADDR="http://127.0.0.1:8200"
export VAULT_TOKEN="root"
python examples/engines/pki.py
```

### Databases

```bash
export VAULT_ADDR="http://127.0.0.1:8200"
export VAULT_TOKEN="root"
python examples/engines/database.py
```
