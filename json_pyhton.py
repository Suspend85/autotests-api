# user_data = {
# 	"name": "Иван",
# 	"age": 30,
# 	"is_student": False,
# 	"courses": ["Python", "QA Autoamtion", "API Testing"],
# 	"address": {
# 		"city": "Moscow",
# 		"zip": "1010100",
# 		"point": {"name": "house"}
# 	}
# }

import json

json_data = """{
  "name": "Иван",
  "age": 30,
  "is_student": true,
  "courses": ["Python", "QA Autoamtion", "API Testing"],
  "address": {
    "city": "Moscow",
    "zip": "1010100",
    "point": {"name": "house"}
  }
}
"""
parsed_data = json.load(json_data) # Преобразуем JSON-строку в Python-объект (dict)
print(parsed_data)
print(type(parsed_data))
print(parsed_data['name'])
print(parsed_data['age'])
print(parsed_data['courses'])
print(parsed_data['address']['city'])
print(parsed_data['address']['zip'])

data = {'name': 'Мария',
		'age': 25,
		'is_student': True,
		'another': None
		}

json_string = json.dumps(data, indent=4)
print(json_string, type(json_string))

with open("json_example.json", "r", encoding="utf-8") as f:
	read_data = json.load(f)
	print(read_data, type(read_data))

with open("json_user.json", "w", encoding="utf-8") as f:
	json.dump(data, f, indent=2, ensure_ascii=False)
