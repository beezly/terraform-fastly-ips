data "external" "fastly_ip_addresses" {
  program = ["${path.module}/get_fastly_addresses.py"]
}
