#!/usr/bin/env python

import requests
import json

#headers = {"Content-Type": "application/json"}
url="http://192.168.1.162/api/qG5Y5IyFuKus5eia9-7XPnISd4hhWiHfZd-KS5Ve/lights/3/state", headers = {"Content-Type": "application/j
son"},
data = json.dumps({'on':True, 'sat':254, 'bri':254,'hue':10000})
r = requests.put(url, data)

print r.json
