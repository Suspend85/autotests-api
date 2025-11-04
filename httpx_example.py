import httpx
from httpx import request

# response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
# print(f'Response from server: {response.status_code}')
# print(f'Response from server: {response.json()}')
#

# data = {
# 	"title": "New task",
# 	"completed": False,
# 	"userID": 1
# }
# response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)
# print(f'jsonplaceholder statuscode: {response.status_code}')
# print(f'jsonplaceholder json: {response.json()}')
#
#
# data2 = {
# 	"username": "test_user", "password": "123456"
# }
# response = httpx.post('https://httpbin.org/post', data=data2)
# print(f'httpbin statuscode: {response.status_code}')
# print(f'httpbin json: {response.json()}')
#
#
# headers = {
# 	"Authorization": "Bearer 123456",
# 	"content-type": "application/json"
# }
# response = httpx.get('https://httpbin.org/get', headers=headers)
#
# print(response.request.headers)
# print(response.json())


# params = {"userId": 1}
# response = httpx.get('https://jsonplaceholder.typicode.com/todos', params=params)
# print(response.url)
# print(response.json())


# files = {"file": ('example.txt', open("example.txt", 'rb'))}
# response = httpx.post('https://httpbin.org/post', files=files)
# print(response.json())


# with httpx.Client() as client:
# 	response1 = client.get('https://jsonplaceholder.typicode.com/todos/1')
# 	response2 = client.get('https://jsonplaceholder.typicode.com/todos/2')
#
# print(response1.json())
# print(response2.json())


# client = httpx.Client(headers={"Authorization": "Bearer 123456"})
# response = client.get('https://httpbin.org/get')
# print(response.json())

# try:
# 	response = httpx.get('https://jsonplaceholder.typicode.com/invalid-url')
# 	print(response.status_code)
# 	response.raise_for_status()
# except httpx.HTTPStatusError as e:
# 	print(f'Request error: {e}')


try:
	response = httpx.get('https://httpbin.org/delay/5', timeout=2)
	print(response.status_code)
	response.raise_for_status()
except httpx.ReadTimeout:
	print('Request timeout')