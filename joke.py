import requests
import json
from pprint import pprint

url = "https://icanhazdadjoke.com/"

payload = {}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data = payload)

print("Here is your dad approved joke:")

responseJson = response.json()

pprint(response.text.encode('utf8'))
