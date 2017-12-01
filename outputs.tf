output "public-ip-list" {
  value = "${values(data.external.fastly_ip_addresses.result)}"
  description = "IP address ranges returned by Fastly's Public IP List API"
}

