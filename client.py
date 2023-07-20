import requests

url = "http://localhost:8000/secure_endpoint/"
api_key = "admin" 

headers = {
    "Content-Type": "application/json",
    "X-API-KEY-Token": api_key
}

data = {
    "user_message": "Hello"
}
response = requests.post(url, headers=headers, json=data)
print(response.json())

while True:
    message = input("question: ")
    data ["user_message"] = message
    response = requests.post(url, headers=headers, json=data)
    print(response.json())
