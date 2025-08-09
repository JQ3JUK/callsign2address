#!/usr/bin/env python3

import sys
import requests
import xml.etree.ElementTree as ET
import csv

# コールサイン読み込み
args = sys.argv
with open(args[1], 'r') as f:
	callsigns = f.readlines()

# qrz.comキー取得
# https://www.qrz.com/page/current_spec.html
endpoint = 'https://xmldata.qrz.com/xml/current/'
ns = {'qrz' : 'http://xmldata.qrz.com'}
session = requests.post(endpoint, data={'username': '[your callsign]', 'password': '********', 'agent': 'callsign2address'})
root = ET.fromstring(session.text)
key = root.find("qrz:Session", ns).find("qrz:Key", ns).text

# qrz.comデータ取得・CSV出力
keys = ['call', 'fname', 'name', 'addr1', 'addr2', 'state', 'zip', 'country']
prefixed = list(map(lambda x: "qrz:" + x, keys))
with open(args[1] + '.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['callsign', 'name', 'addr1', 'addr2', 'state', 'zipcode', 'country'])
	for callsign in callsigns:
		xml = requests.post(endpoint, data={'s': key, 'callsign': callsign.strip()})
		root = ET.fromstring(xml.text)
		data = root.find("qrz:Callsign", ns)
		values = list(map(lambda x: data.find(x, ns).text if data.find(x, ns) is not None else "", prefixed))

		writer.writerow([values[0], values[1] + ' ' + values[2], values[3], values[4], values[5], values[6], values[7].upper()])
