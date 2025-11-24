from jsonschema import validate

schema = {
	"type": "object",
	"properties": {
		"name": {"type": "string"},
		"age": {"type": "integer"},
	},
	"required": ["name"]
}

data = {
	"name": "Alice",
	"age": 30
}

validate(data, schema=schema)

