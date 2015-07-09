#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# imagga_tag_upload_file.py
# Upload file to imagga service and get the result of tag
#
# Author : sosorry
# Date   : 18/04/2015

import requests
import json

url = "http://api.imagga.com/v1/content"
files = {"file": open("/home/pi/image.jpg", "rb")}

headers = { 
    "accept": "application/json",
    "authorization": "Basic YWNjXzJkYzdkNzNjMmYwODliMToxYzQ3Yzg2ZDg0YjdmYjdjYjZjNzQ1NTQ1MmYwNTgzMQ=="
    }   
response = requests.post(url, files=files, headers=headers)
print(response.text)
data = json.loads(response.text.encode("ascii"))
print(data["uploaded"][0]["id"])

url = "http://api.imagga.com/v1/tagging"
querystring = {"content": data["uploaded"][0]["id"]}
response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text.encode("ascii"))
print(data["results"][0]["tags"][0]["tag"].encode("ascii"))
