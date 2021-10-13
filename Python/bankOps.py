import sys
class Customer:
    '''Customer class with bank related application'''
    bankName='AnyRandomBankOFAnywhere'
    def __init__(self,name,age,sex,balance=0):
        self.name = name
        self.age=age
        self.sex=sex
        self.balance=balance

    def deposit(self,amt):
        self.balance = self.balance + amt
        print(f"After deposite of {amt} your current balance is :",self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficient balance!!")
            sys.exit()
        else:
            self.balance = self.balance - amt
            print(f"After withdrawl of {amt},your current balance is :",self.balance)
print("Welcome to ",Customer.bankName)
name = input("Enter your name:  ")
age = input("Enter your age:  ")
gender = input("Enter your gender:  ")
c = Customer(name,age,gender)
while(True):
    print("Enter d-deposit \n w-withdraw \n e-exit")
    option = input("Enter your choice here:  ")
    if option=="d" or option=="D":
        amt =float(input("Enter the amount to deposit:  "))
        c.deposit(amt)
    elif option=="w" or option== "W":
        amt= float(input("Enter the amount you want to deposit:  "))
        c.withdraw(amt)
    elif option=="e" or option=="E":
        print("Thanks for banking")
        sys.exit()