import time

import httpx

from tools.fakers import fake

BASE = 'http://localhost:8000'

create_user_payload = {
	"email": fake.email(),
	"password": "tester",
	"lastName": "Let",
	"firstName": "Vasya",
	"middleName": "Nikolayevich"
}

create_user_response = httpx.post(f'{BASE}/api/v1/users', json=create_user_payload)
create_user_response_data = create_user_response.json()
print(f'Create user data: {create_user_response_data}')

login_payload = {
	"email": create_user_payload['email'],
	"password": create_user_payload['password'],
}
login_response = httpx.post(f'{BASE}/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
print(f'Login data: {login_response_data}')

update_user_headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
update_user_data = {
	"email": fake.email(),
	"lastName": f"string{time.time()}",
	"firstName": f"string{time.time()}",
	"middleName": f"string{time.time()}"
}

update_user_response = httpx.patch(
	f'{BASE}/api/v1/users/{create_user_response_data["user"]["id"]}',
	json=update_user_data,
	headers=update_user_headers
)
print(f'Update user data: {update_user_response.status_code}')
