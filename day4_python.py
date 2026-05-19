# Function Basics

def greet(name):
    return f"Hello, {name}!"

print (greet("Imran"))

def greet(name = "World"):
    return f"Hello, {name}!"

print (greet("Imran"))

def min_max(number):
    return min(number), max(number)
numbers = [3, 0, 4, 1, 5, 9]

print(f"Min: {min_max(numbers)[0]}, Max: {min_max(numbers)[1]}")

# List Basics

fruits = ["apple", "banana", "mango", "grape", "orange"]
fruits.append("blueberry")
fruits.remove("banana")
print(fruits)
print(fruits[0])
print(fruits[-1])

for fruit in fruits:
    print(f"I like {fruit}!")

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# List Comprehensions

numbers = [1,2,3,4,5]
squares = [x ** 2 for x in numbers]
even = [x for x in numbers if x % 2 == 0]

print(f"Squares: {squares}")
print(f"Even: {even}")

# Dictionary Basics

person = {
    "name": "Imran",
    "age": 21,
    "course": "Computer Systems Engineering"
}

print(person["name"])
print(person.get("age"))
print(person.get("salary", "Not Available"))

person["university"] = "Brunel University of London"
person["Salary"] = 3000

for key, value in person.items():
    print(f"{key}: {value}")

expenses = [
    {"name": "Rent", "amount": 1200},
    {"name": "Groceries", "amount": 400}
]

total = sum(ex["amount"] for ex in expenses)
print(f"Total Expenses: £{total}")

def get_savings(salary, expenses):
    total_expenses = sum(ex["amount"] for ex in expenses)
    return salary - total_expenses

def main():
    y = person["Salary"]
    x = expenses
    savings = get_savings(y, x)
    print(f"Monthly Savings: £{savings}")

if __name__ == "__main__":
    main()

# Conditionals

score = 70

if score >= 70:
    print("Grade: A")
elif score >= 60:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Grade: F")

# Error Handling

def divide(a, b):
    try: 
        result = a/b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Invalid input type."

print(divide(10,2))
print(divide(10,0))
print(divide(10,"x"))

# String Manipulation

name = "  Operation Job  "
print(name.strip())
print(name.upper())
print(name.lower())
print(name.strip().upper())

sentence = "Python is great for automation"
print(sentence.split(" "))
print(sentence.replace("great", "essential"))
print("Python" in sentence)
print(sentence.startswith("Python"))
print(len(sentence))

# File I/O

# Writing to a file
with open("test.txt", "w") as f:
    f.write("Line 1: Operation Job\n")
    f.write("Line 2: Python Programming\n")

# Reading from a file
with open("test.txt", "r") as f:
    content = f.read()
    print(content)

# Appending to a file
with open("test.txt", "a") as f:
    f.write("Line 3: File Handling\n")

# Reading the updated file
with open("test.txt", "r") as f:
    content = f.read()
    print(content)

