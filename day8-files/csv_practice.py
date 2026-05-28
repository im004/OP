import csv

# Writing a CSV file
expenses = [
    {"name": "Rent", "amount": 900, "category": "Housing"},
    {"name": "Food", "amount": 300, "category": "Food"},
    {"name": "Transport", "amount": 150, "category": "Travel"},
]

with open("expenses.csv", "w", newline="") as f:
    fieldnames = ["name", "amount", "category"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(expenses)

print("CSV written")

# Reading a CSV file
with open("expenses.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']}: £{row['amount']} ({row['category']})")

# Calculate total from CSV
with open("expenses.csv", "r") as f:
    reader = csv.DictReader(f)
    total = sum(float(row["amount"]) for row in reader)
    print(f"Total from CSV: £{total:.2f}")