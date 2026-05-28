import json

user_data = {
    "name": "Imran",
    "age": 21,
    "skills": ["Python", "Git", "Linux", "IoT Systems"],
    "projects": [
        {"name": "Budget Tracker", "description": "A simple budget tracking app in Python."},
        {"name": "IoT Weather Station", "description": "A weather station using Raspberry Pi and sensors."},
        {"name": "Personal Portfolio", "description": "A personal website showcasing projects and skills."}
    ],
    "address": {
        "street": "Uxbridge Road",
        "city": "London",
        "country": "UK"
    },
    "active": True     
}

with open("user_data.json", "w") as f:
    json.dump(user_data, f, indent=4)

print("User data saved to 'user_data.json'")

with open("user_data.json", "r") as f:
    loaded_data = json.load(f)
print("\nLoaded user data:")
print(loaded_data)

print(loaded_data["name"])
print(loaded_data["skills"][1])
print(loaded_data["projects"][2]["description"])
print(loaded_data["active"])

# Dictionary → JSON string
json_string = json.dumps(user_data, indent=2)
print(json_string)
print(type(json_string))  # <class 'str'>

# JSON string → dictionary
parsed = json.loads(json_string)
print(type(parsed))  # <class 'dict'>
print(parsed["skills"])