import csv
import json
import os
from budget_with_json import load_budget, save_budget

def read_expenses(filename):
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)

def calculate_category_totals(expenses):
    totals = {}
    for e in expenses:
        cat = e["category"]
        amt = float(e["amount"])
        totals[cat] = totals.get(cat, 0) + amt
    return totals

def save_report(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Report saved to '{filename}'")

def load_report(filename):
    with open(filename, "r") as f:
        return json.load(f)

def main():
    # Load expenses from CSV
    expenses = read_expenses("expenses.csv")
    
    # Calculate totals by category
    category_totals = calculate_category_totals(expenses)
    
    # Load existing budget data
    budget_data = load_budget()
    
    # Prepare report data
    report = {
        "income": budget_data["income"],
        "category_totals": category_totals,
        "total_spent": sum(category_totals.values()),
        "remaining": budget_data["income"] - sum(category_totals.values())
    }

    live = load_report("budget_report.json") if "budget_report.json" in os.listdir() else None
    if live:
        print("Loaded existing report:")
        print(json.dumps(live, indent=4))
    else:        print("No existing report found, creating new one.")

    # Save report to JSON
    save_report(report, "budget_report.json")

if __name__ == "__main__":
    main()