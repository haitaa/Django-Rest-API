import requests

#endpoint = "https://httpbin.org/status/200"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={'title': "Hello World"}) 
print(get_response.json())

#print(get_response.json()['message'])
#print(get_response.status_code)