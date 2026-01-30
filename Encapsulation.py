#encapsulation
class Student:
    def __init__(self,marks):
        self.__marks=marks #making the marks private

    def get_marks(self):  #fetching the private variable
        return self.__marks

    
    
s1=Student(100)
print("Original marks:",s1.get_marks())


#creat a class bank balance in which balance is hidden and only user can acces it

class BankBalance():
    def __init__(self,balance):
        self.__balance=balance

    def get_balance(self):
        return self.__balance
    
b1=BankBalance(2000)
print("Balance is:",b1.get_balance())

#set the marks
class Student:
    def __init__(self,marks):
        self.__marks=marks #making the marks private

    def get_marks(self):  #fetching the private variable
        return self.__marks
    def set_marks(self,new_marks):
        self.__marks=new_marks
s1=Student(100)
s1.set_marks(90)
print("new marks:",s1.get_marks())
        
