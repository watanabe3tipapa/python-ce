#! /usr/bin/env python3
import requests
import urllib.parse

query = "北海道/小樽市"

url = "https://geolonia.github.io/japanese-addresses/api/ja/"
data = requests.get(url + urllib.parse.quote(query) + ".json").json()
for i, x in enumerate(data):
    print(i + 1, x)
