from src.account import Expense

class BudgetTracker:
    def __init__(self, income):
        if income < 0:
            raise ValueError("Income must be non-negative.")
        self.income = income
        self.expenses = []

    def add_expense(self, name, amount, category):
        expense = Expense(name, amount, category)
        self.expenses.append(expense)
        print(f"Added expense: {expense}")

    def total_expenses(self):
        return sum(e.amount for e in self.expenses)
    
    def total_spent(self):
        return self.total_expenses()
    
    def remaining_budget(self):
        return self.income - self.total_expenses()
    
    def category_breakdown(self):
        breakdown = {}
        for e in self.expenses:
            breakdown[e.category] = breakdown.get(e.category, 0) + e.amount
        return breakdown
    
    def summary(self):
        print("\n-------- Budget Summary --------")
        for e in self.expenses:
            print(f"  {e}")
        print(f"\nTotal Income:  £{self.income:.2f}")
        print(f"Total Spent:   £{self.total_spent():.2f}")
        print(f"Remaining:     £{self.remaining_budget():.2f}")

        print("\n-------- Category Breakdown --------")
        for category, total in self.category_breakdown().items():
            print(f"  {category}: £{total:.2f}")

        if self.remaining_budget() < 0:
            print("\n⚠️  Over budget!")
        else:
            print("\n✅ Within budget.")

    def save(self, filename = "budget_summary.txt"):
        with open(filename, "w") as f:
            f.write("-------- Budget Summary --------\n")
            for e in self.expenses:
                f.write(f"  {e}\n")
            f.write(f"\nTotal Income:  £{self.income:.2f}\n")
            f.write(f"Total Spent:   £{self.total_expenses():.2f}\n")
            f.write(f"Remaining:     £{self.remaining_budget():.2f}\n")

            f.write("\n-------- Category Breakdown --------\n")
            for category, total in self.category_breakdown().items():
                f.write(f"  {category}: £{total:.2f}\n")

            if self.remaining_budget() < 0:
                f.write("\n⚠️  Over budget!\n")
            else:
                f.write("\n✅ Within budget.\n")
