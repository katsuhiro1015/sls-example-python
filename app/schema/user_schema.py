INPUT = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "type": "object",
    "examples": [{"id": "1", "name": "yosistamp", "age": 20}],
    "required": ["id", "name"],
    "properties": {
        "id": {"type": "string", "pattern": "[a-zA-Z0-9-_]+", "length": 12},
        "name": {"type": "string", "minLength": 0, "maxLength": 50},
        "num": {"type": "integer", "minimum": 0, "maximum": 199},
    },
}

