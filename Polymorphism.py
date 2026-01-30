#polymorphism-->same methode name,diffrent behaivior depends on object
#one name many forms
class Human:
    def speak(self):
        print("Human is speaking")
class Baby:
    def speak(self):
        print("baby is crying")
class dog:
    def speak(self):
        print("dog is barking")

#polymorphism in action
h=Human()
b=Baby()
d=dog()

h.speak()
b.speak()
d.speak()

#create a class car ,bike ,truck and print something
class car:
    def move(self):
        print("car is moving")

class bike:
    def move(self):
        print("bike is running")
class truck:
    def move(self):
        print("truck is killing")

c=car()
b=bike()
t=truck()

c.move()
b.move()
t.move()

#creat a class person with methode Role,create two child Student-print (i am student) teacher- (i am teacher)
#then create another class assistant this inharited from both student and teacher
#1.create an object of assistatnt
#2.call role
#3.obser which methode is called
class Person:
    def Role(self):
        print("Role of Everyone")

class Student(Person):
    def Role(self):
        print("i am a student")
class Teacher(Person):
    def Role(self):
        print("i am teacher")

class Assistant(Student,Teacher):
    pass

A=Assistant()
A.Role()
        
































