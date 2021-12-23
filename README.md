# Python Vault Examples

```bash
virtualenv venv
source venv/bin/activate
pip install -r pip-reqs.txt
```

```bash
vault-ent server -dev -dev-root-token-id=root -log-level=debug
```

```bash
export VAULT_ADDR="http://127.0.0.1:8200"
export VAULT_TOKEN="root"
```

```bash
cd setup/
./setup.sh
```

## Auth Methods

### AppRole

```bash
export APPROLE_ROLE_ID=$(vault read -format=json auth/approle/role/example-approle/role-id | jq -r .data.role_id)
export APPROLE_SECRET_ID=$(vault write -format=json -f auth/approle/role/example-approle/secret-id | jq -r .data.secret_id)

echo $APPROLE_ROLE_ID
echo $APPROLE_SECRET_ID
```

```bash
python auth/approle.py
```

## Secrets Engines

### KV

```bash
python engines/kv.py
```

### Transit

```bash
python engines/transit.py
```

### PKI

```bash
python engines/pki.py
```

### Databases

```bash
python engines/database.py
```
# vault-python-examples
