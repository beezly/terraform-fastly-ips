#!/usr/bin/env python3
"""
Util to grab Fastly Inbound addresses 
"""
import os
import urllib.request
import json
import hashlib

FASTLY_IP_API = 'https://api.fastly.com/public-ip-list'

def get_fastly_ips(api=FASTLY_IP_API):
    """
    Gets an Array of IPs from Fastly which represent the inbound request addresses that fastly will use
    :param api: Fastly IP API
    :type rg_name: str
    :return: Array of IP ranges
    """
    with urllib.request.urlopen(api) as url:
      data = json.loads(url.read().decode())
      return dict((hashlib.new('md5',v.encode()).hexdigest(),v) for v in data['addresses'])

if __name__ == "__main__":
    print(json.dumps(get_fastly_ips()))
