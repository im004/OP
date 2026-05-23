import os
import sys
import math
import random
import datetime
import json

# os — interact with the operating system
print(os.getcwd())           # current directory
print(os.listdir("."))       # list files in current dir
os.makedirs("test_folder", exist_ok=True)  # create folder

# math
print(math.sqrt(144))
print(math.floor(3.9))
print(math.ceil(3.1))

# random
print(random.randint(1, 100))
print(random.choice(["apple", "banana", "mango"]))

# datetime
now = datetime.datetime.now()
print(now.strftime("%d/%m/%Y %H:%M"))

# json
data = {"name": "Imran", "age": 21, "skills": ["Python", "Git"]}
json_string = json.dumps(data, indent=2)
print(json_string)
parsed = json.loads(json_string)
print(parsed["name"])