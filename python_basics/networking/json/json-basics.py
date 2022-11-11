import requests
import json
from requests.exceptions import HTTPError

jsondict = {}


def retrievejson(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        # access JSOn content
        jsonResponse = response.json()
        print("Entire JSON response")
        print(jsonResponse)
        return jsonResponse

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


jsonData = retrievejson('https://httpbin.org/get')

for key, value in jsonData.items():
    jsondict[key] = value

print(jsondict["headers"])


