class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"Account owner: {self.owner} | Balance: {self.balance}"
     

account_1 = BankAccount("Imran", 13000)
account_2 = BankAccount("Ali", 5000)

print(account_1)
print(account_2)    

account_1.deposit(4000)  
account_2.withdraw(2000)

print(account_1)
print(account_2)   


#-----------------------------------------------------------------------------

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"{self.name} makes a sound")
    
    def __str__(self):
        return f"{self.name} is a {self.species}"
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed
    
    def speak(self):
        print(f"{self.name} barks") 

    def fetch(self):
        print(f"{self.name} fetches the ball!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, species="Cat")
    
    def speak(self):
        print(f"{self.name} meows")

dog_1 = Dog("Jurrien", "Labrador")
Cat_1 = Cat("Whiskers")

dog_1.speak()
Cat_1.speak()
dog_1.fetch()

animals = [dog_1, Cat_1]

for animal in animals:
    print(animal)
    animal.speak()

