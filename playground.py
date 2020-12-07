#!/usr/bin/python

import json

# source dev key
with open('key.json') as file:
  dev = json.load(file)

key = dev["key"]
print("dev key: " + key)
