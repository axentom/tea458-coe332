import requests

response = requests.get(url="http://localhost:5004/animals")

#let's look at the response code

print(response.status_code)
print(response.json())
print(response.headers)
