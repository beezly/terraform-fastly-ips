# Fastly IP address ranges

Acts as a datasource for the fastly IP address API at https://api.fastly.com/public-ip-list

## Usage

Import this module's outputs in your data-sources.tf:

```
module "fastly-ips" {
  source "beezly/public-ip-list/fastly"
}
```

and then refer to the Fastly IP address ranges with `module.fastly-ips.public-ip-list`


