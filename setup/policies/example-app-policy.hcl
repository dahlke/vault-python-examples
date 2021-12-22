path "secret/*" {
  capabilities = ["list"]
}

path "secret/data/*" {
  capabilities = ["list"]
}

path "secret/metadata/applications/" {
  capabilities = ["list", "read"]
}

path "secret/data/applications/" {
  capabilities = ["list", "read"]
}

path "secret/data/applications/example-app" {
  capabilities = ["list", "read", "create", "update"]
}
