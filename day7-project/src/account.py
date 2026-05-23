class Expense:
    def __init__(self, name, amount, category):
        if amount < 0:
            raise ValueError("Expense amount must be non-negative.")
        self.name = name
        self.amount = amount
        self.category = category
    
    def __str__(self):
        return f"Expense: {self.name} | Amount: {self.amount} | Category: {self.category}"