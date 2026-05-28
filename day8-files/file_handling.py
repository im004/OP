with open("notes.txt", "w") as f:
    f.write("Line 1: Operation Job\n")
    f.write("Line 2: Day 8 - File Handling\n")

with open("notes.txt", "r") as f:
    content = f.read()
    print(content)

with open("notes.txt", "a") as f:
    f.write("Line 3: Practice with files\n")

with open("notes.txt", "r+") as f:
    content = f.read()
    print(f"File has {len(content)} characters.")
    f.write("\nLine 4: Updated content")
    print(content)

# Read all lines into a list
with open("notes.txt", "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        print(f"{i+1}: {line.strip()}")

# More memory-efficient for large files
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())

import os

def read_file_safe(filename):
    if not os.path.exists(filename):
        print(f"File '{filename}' not found")
        return None
    with open(filename, "r") as f:
        return f.read()

content = read_file_safe("notes.txt")
content_missing = read_file_safe("doesnt_exist.txt")


