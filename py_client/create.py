import requests


headers = {"Authorization": 'Bearer 1e0d68a1559cc0b416c9d2bc28ec313d434e4cbf'}
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "PS4",
    "price": 32.99
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())