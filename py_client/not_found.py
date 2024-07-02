import requests

endpoint = "http://localhost:8000/api/products/893724347329847219/"

get_response = requests.get(endpoint)
print(get_response.json())