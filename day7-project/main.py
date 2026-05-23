from src.tracker import BudgetTracker

def main():
    try:
        income = float(input("Enter monthly income: £"))
        tracker = BudgetTracker(income)

        while True:
            name = input("Expense name (or 'done'): ")
            if name.lower() == 'done':
                break
            category = input("Category: ")
            amount = float(input("Amount: £"))
            tracker.add_expense(name, amount, category)

        tracker.summary()
        tracker.save()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()