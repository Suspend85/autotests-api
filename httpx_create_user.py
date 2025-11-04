import httpx
from tools.fakers import get_random_email

payload = {
  "email": get_random_email(),
  "password": "tester",
  "lastName": "Let",
  "firstName": "Vasya",
  "middleName": "Nikolayevich"
}

response = httpx.post('http://localhost:8000/api/v1/users', json=payload)

print(response.status_code)
print(response.json())
