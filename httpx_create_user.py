import httpx
from tools.fakers import fake

payload = {
  "email": fake.email(),
  "password": "tester",
  "lastName": "Let",
  "firstName": "Vasya",
  "middleName": "Nikolayevich"
}

response = httpx.post('http://localhost:8000/api/v1/users', json=payload)

print(response.status_code)
print(response.json())
