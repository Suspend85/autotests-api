import json

import httpx


login_payload = {
  "email": "tester@example.com",
  "password": "tester"
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()

print(f'Login response: {login_response_data}')
print(f'Status code: {login_response.status_code}')

access_token_payload = login_response_data['token']['accessToken']
headers = {"Authorization": f"Bearer {access_token_payload}"}

users_response = httpx.get(
	'http://localhost:8000/api/v1/users/me',
	headers=headers,
	timeout=10
)

users_response_data = users_response.json()
print(f'users response: \n{json.dumps(users_response_data, indent=2, ensure_ascii=False)}')
print(f'Status code: {users_response.status_code}')


