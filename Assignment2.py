import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users"
#Read Input
open_file = open("C:\\Users\\hasee\\Desktop\\API\\CreateUser.json", 'r')
input_json = open_file.read()
json_request = json.loads(input_json)
# Make POST request with Json Input body
responsee= requests.post(url, json_request)
print(responsee.content)

assert responsee.status_code == 201

print(responsee.headers.get('Content-Length'))

json_response=json.loads(responsee.text)

id = jsonpath.jsonpath(json_response, 'id')

print(id[0])
