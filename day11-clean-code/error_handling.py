# class BudgetError(Exception):
#     """Base class for exceptions in this module."""
#     pass

# class NegativeAmountError(BudgetError):
#     """Raised when a negative amount is provided."""
#     pass

# class InsufficientFundsError(BudgetError):
#     """Raised when trying to withdraw more than the available balance."""
#     pass

# class InvalidCurrencyError(BudgetError):
#     """Raised when an invalid currency code is used."""
#     pass

# def withdraw(amount, balance):
#     if amount < 0:
#         raise NegativeAmountError("Amount cannot be negative.")
#     if amount > balance:
#         raise InsufficientFundsError(f"Cannot withdraw £{amount} from balance of £{balance}" + "\n" + "Cannot withdraw more than the available balance.")
#     return balance - amount

# try:
#     new_balance = withdraw(200, 100)
# except NegativeAmountError as e:
#     print(f"Error: {e}")
# except InsufficientFundsError as e:
#     print(f"Error: {e}")
# except BudgetError as e:
#     print(f"An error occurred: {e}")

# def read_config(filename):
#     f = None
#     try:
#         f = open(filename, 'r')
#         return f.read()
#     except FileNotFoundError:
#         print(f"Error: The file '{filename}' was not found.")
#     except PermissionError:
#         print(f"Error: You do not have permission to read the file '{filename}'.")
#     finally:
#         if f:
#             f.close()
#         print("Finished attempting to read the configuration file.")

# def read_config_clean(filename):
#     try:
#         with open(filename, "r") as f:
#             return f.read()
#     except FileNotFoundError:
#         print(f"Config file '{filename}' not found")
#         return None
    
# import logging

# logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# logger = logging.getLogger(__name__)

# def divide(a, b):
#     logger.info(f"Dividing {a} by {b}")
#     try:
#         result = a / b
#         logger.info(f"Result: {result}")
#         return result
#     except ZeroDivisionError:
#         logger.error("Division by zero attempted")
#         return None

# result = divide(10, 0)
# print(f"Division result: {result}")

from typing import Optional

def greet(name: str) -> str:
    return f"Hello, {name}!"

def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def find_user(user_id: int) -> Optional[dict]:
    # Optional means it can return dict OR None
    users = {1: {"name": "Imran"}, 2: {"name": "Ali"}}
    return users.get(user_id)


def update_scores(
    student: str,
    scores: list[int],
    passing_grade: int = 50
) -> dict[str, bool]:
    return {
        subject: score >= passing_grade
        for subject, score in zip(["Maths", "English", "Science"], scores)
    }


# Test them
print(greet("Imran"))
print(calculate_average([85.0, 92.5, 78.0]))
print(find_user(1))
print(find_user(2))
print(update_scores("Imran", [75, 45, 88]))

def convert_currency(
    amount: float,
    from_currency: str,
    to_currency: str,
    rates: dict[str, float]
) -> Optional[float]:
    """
    Convert an amount from one currency to another.

    Args:
        amount: The amount to convert (must be positive)
        from_currency: The source currency code (e.g. 'GBP')
        to_currency: The target currency code (e.g. 'USD')
        rates: Dictionary of exchange rates with base currency

    Returns:
        The converted amount rounded to 2 decimal places,
        or None if either currency is not found in rates

    Raises:
        ValueError: If amount is negative

    Example:
        >>> convert_currency(100, 'GBP', 'USD', {'USD': 1.27})
        127.0
    """
    if amount < 0:
        raise ValueError("Amount must be positive")
    if from_currency not in rates or to_currency not in rates:
        return None
    in_base = amount / rates[from_currency]
    return round(in_base * rates[to_currency], 2)