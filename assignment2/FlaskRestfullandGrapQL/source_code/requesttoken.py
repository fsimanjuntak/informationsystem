import json
import urllib2
import requests


data = {
        "username": "frans",
    "password": "testingapi"
}

response = requests.post('http://127.0.0.1:5000/auth', json=data)

# For successful API call, response code will be 200 (OK)
if(response.ok):
    json_data = json.loads(response.content)
    print(json_data)
else:
  # If response code is not ok (200), print the resulting http error code with description
    response.raise_for_status()
