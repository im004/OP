import json
import os

SAVE_FILE = "budget_data.json"

def load_budget():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return {"income": 0, "expenses": []}

def save_budget(data):
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Budget data saved to '{SAVE_FILE}'")

def show_summary(data):
    total = sum(e["amount"] for e in data["expenses"])
    print(f"\nIncome: £{data['income']:.2f}")
    print(f"Spent:  £{total:.2f}")
    print(f"Left:   £{data['income'] - total:.2f}")
    for e in data["expenses"]:
        print(f"  {e['name']} ({e['category']}): £{e['amount']:.2f}")

def main():
    data = load_budget()

    print("Welcome to the Budget Tracker!")

    if data["income"] == 0:
        data["income"] = float(input("Enter monthly income: £"))

    while True:
        name = input("Expense name (or 'done'): ")
        if name.lower() == "done":
            break
        category = input("Category: ")
        amount = float(input("Amount: £"))
        data["expenses"].append({
            "name": name,
            "amount": amount,
            "category": category
        })

    show_summary(data)
    save_budget(data)

if __name__ == "__main__":
    main()

