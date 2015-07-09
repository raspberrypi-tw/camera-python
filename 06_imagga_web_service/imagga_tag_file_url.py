#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# imagga_tag_file_url.py
# Send image url to imagga and get the result of tag
#
# Author : sosorry
# Date   : 18/04/2015

import requests
import json

url = "http://api.imagga.com/v1/tagging"
querystring = {"url":"http://playground.imagga.com/static/img/example_photo.jpg"}
headers = {
    "accept": "application/json",
    "authorization": "Basic YWNjXzJkYzdkNzNjMmYwODliMToxYzQ3Yzg2ZDg0YjdmYjdjYjZjNzQ1NTQ1MmYwNTgzMQ=="
    }
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)

data = json.loads(response.text.encode("ascii"))
print(data["results"][0]["tags"][0]["tag"].encode("ascii"))
