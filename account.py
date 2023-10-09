"""
# Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functional.
"""

class Bankaccount:
  def __init__(self):
    self.balance=0
    print("Bankaccount Details")
  def deposit(self):
    amount=float(input("Enter the amount:"))
    self.balance+=amount
    print("amount is deposited in your account", amount)
  def withdraw(self):
      amount=float(input("Enter the amount:")) 
      if self.balance>=amount:
        self.balance-=amount 
        print("your withdraw:", amount)
      else:
        print("you don't have enough money")
  def display(self):
      print("Available Balance:", self.balance)
s=Bankaccount()
s.deposit()
s.withdraw()
s.display()
    