#!/usr/bin/python 

from w3af_api_client import Connection, Scan, traffic
import requests
import re
import inspect

# Connect to the REST API and get it's version
conn = Connection('http://127.0.0.1:5000/')
print conn.get_version()

#scan = Scan(conn)
#scan.start(scan_profile, target_urls)
scans = conn.get_scans()
for scan in scans:
#	print scan.get_urls()
	for x in scan.get_findings():
		for y in x.resource_data:
			print y, ": ", x.resource_data[y]	
		try:
			traffic = x.get_traffic()
			for i in (traffic):
				print "Request: ", i.response, "\n"
				print "Response: ", i.request, "\n"
		except:
			print "No data, check manually the provided link"
	break

		
