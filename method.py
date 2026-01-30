#method is function which is related to object
'''class Student:
    def __init__(self,name):
        self.name=name

    def hello(self):
        print("Welcome",self.name)
s1=Student("Rahul")
s1.hello()'''

'''class Student:
    def __init__(self,name):
        self.name=name

    def hello(self):
        print("Welcome",self.name)
    @staticmethod #static methode no need to put any arguments in function collegeNmae
    def collegeName():
        print("This is LPU")
s1=Student("Karan")
s1.hello()
s1.collegeName()'''

#create a class stu such that object atri as name and marks there is a normal methode which will dishplay to print Hi name marks
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print("Hi",self.name,"Your marks ",self.marks)

s1=Student("Rahul",56)
s1.display()
