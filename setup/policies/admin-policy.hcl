path "secret/*" {
  capabilities = ["create", "list", "read", "update", "delete"]
}

path "secret/data/*" {
  capabilities = ["create", "list", "read", "update", "delete"]
}
