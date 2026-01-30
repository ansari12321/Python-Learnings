#inhariting the properties from more than one class
class Father:
    def work(self):
        #super().work()  -->it wil also run
        print("I do Job")

class Mother:  #if i want to use super() then i have to use in every class so it will not overrite the preveous  
    def work(self):
        #super().work()
        print("I am HouseWife")

class child(Father,Mother):
    def work(self):
        #super().work()
        Father.work(self)
        Mother.work(self)
        print("I go to school\n")

C1=child()
C1.work()

#Methode2 --> same question in simple way
class Father:
    def work(self):
        print("I do job")
class Mother:
    def House(self):
        print("House wife")
class Child(Father,Mother):
    def School(self):
        
        print("I am Student\n")
C1=Child()
C1.work()
C1.House()
C1.School()

#Q3-->
class Teacher:
    def Teaching(self):
        print("Teaching")
class Coder:
    def coding(self):
        print("coding")

class Student(Teacher,Coder):
    def Work(self):
        pass
S1=Student()
S1.Teaching()
S1.coding()

#4-->create a parent a clss in which variable is private and try to acces in child calss
class Parent:
    def __init__(self):
        self.__marks = 85   # private variable

    # getter method (get data)
    def get_data(self):
        return self.__marks


class Child(Parent):
    def show(self):
        data = self.get_data()   # fetching value using another method
        print("Marks:", data)


obj = Child()
obj.show()

#5--> another way of qustion 4(how to acces the priovate variable)
class parent:
    def __init__(self):
        self.__x=30
class child(parent):
    def Show(self):
        print("\n",self._parent__x) #we can use _mainclassname__privateVariable to fetch the private varible from parent class

obj=child()
obj.Show()

#6-->how to acces the protected variable
class parent:
    def __init__(self):
        self._x=15
class Child(parent):
    def show(self):
        print(self._x) #we can access the protected directly by _variablename
obj=Child()
obj.show()

#7-->acces the public varible
class parent:
    def __init__(self):
        self.x=60
class child(parent):
    def Show(self):
        print(self.x) # we can access direcly
obj=child()
obj.Show()







































        

    




    
    






