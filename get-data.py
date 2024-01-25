import json
import requests
import os

apiKey = os.environ.get('HASURA_ADMIN_SECRET')
url = os.environ.get('HASURA_URL')

headers = {
    "Content-Type": "application/json",
    "x-hasura-admin-secret": apiKey,
           }
body = """
query MyQuery {
  ARTIST {
    NAME
    ARTISTID
  }
}



"""
 
response = requests.post(url=url, headers=headers, json={"query": body})
print("response status code: ", response.status_code)
if response.status_code == 200:
    print("\n", json.dumps(json.loads(response.text), indent=2))


