#!/usr/bin/python

from w3af_api_client import Connection, Scan

# Connect to the REST API and get it's version
conn = Connection('http://127.0.0.1:5000/')
print conn.get_version()

# Define the target and configuration
scan_profile = file('./fast_scan.pw3af').read()
target_urls = ['www.ynet.co.il']

scan = Scan(conn)
scan.start(scan_profile, target_urls)

