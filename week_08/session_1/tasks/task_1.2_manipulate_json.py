"""
Task 1.2: Manipulating JSON Data

Goal: Modify JSON data and convert it back to a JSON string.
"""

import json

# Original JSON data
data = {
    "userId": 101,
    "name": "Alice Smith",
    "roles": ["admin", "editor"],
    "isActive": True
}

# TODO: Modify the "isActive" field to False and add "viewer" to the roles list
data["isActive"] = False
data["roles"].append("viewer")

# TODO: Convert the updated data back to a JSON string using json.dumps() and print it
jsonData = json.dumps(data)
print(jsonData)