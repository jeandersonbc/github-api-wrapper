#!/usr/bin/python3
#
# Simple driver to demonstrate usage
#
# Author: Jeanderson Candido
#
import json
import urllib.request as request

from ghwrappers.search import RepositoryQuery


def run(queryable):
    with request.urlopen(queryable.query()) as response:
        return json.loads(response.read().decode())


data = run(RepositoryQuery().lang("java").stars(">=100"))
print("Total items from query:", data["total_count"])

for item in data["items"]:
    print(item["html_url"])

