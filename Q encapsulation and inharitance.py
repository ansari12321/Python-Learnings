#1 create a parent class name person in which name will be private then constructor to set the name then methode getname to return the name
#then make child class name as stident this will inharited from person then it has method show name then print using parent methode
#create onject of student and dishplay tha name
class person:
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name

class Student(person):
    def Show_name(self):
        print(self.get_name())

obj=Student("Rahul")
obj.Show_name()
#methode 2-->
class person:
    def __init__(self):
        self.__name="Hasan"
class Student(person):
    def Show_name(self):
        print(self._person__name)
obj=Student()
obj.Show_name()

#create a parent class account then it should have protected varibale _balance then constroctur should sret the balnce should print balance, child class saving_acount then create a
#methode add money
#and input as amount and show updated balnce

class Account:
    def __init__(self,balance):
        self._balance=balance
        print("initial Balnce:",self._balance)

        
class Saving_account(Account):
    def add_money(self,amount):
        self._balance  += amount #updating the balance
    def Show_updated(self):
        print("After update:",self._balance)

obj=Saving_account(5000)
obj.add_money(1000)
obj.Show_updated()


    
