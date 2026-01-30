#encapsulation question

class BankBalance:
    def __init__(self,balance):
        self.__balance=balance

    def get_balance(self):
        return self.__balance

    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance -=amount
            
        else:
    
            print("Insufficient balance")
            

    def deposit(self,amount):
        if amount>0:
            self.__balance += amount
            print("deposit successful")
            print("Updata balance:",self.__balance)
acc=BankBalance(50000)
acc.deposit(100)
print(acc.get_balance())
