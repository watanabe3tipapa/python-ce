#! /usr/bin/env python3
import requests
import urllib.parse

query = "東京都/港区"

url = "https://geolonia.github.io/japanese-addresses/api/ja/"
data = requests.get(url + urllib.parse.quote(query) + ".json").json()
for i, x in enumerate(data):
    print(i + 1, x)
