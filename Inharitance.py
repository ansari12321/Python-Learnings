#1.Inharitance-->one class uses another class features
class Human: #parent class
    def eat(self):
        print("Human can eat")

class Student(Human):  #child class
    def study(self):
        print("Student can Study \n")

s1=Student()
s1.eat()
s1.study()

#2.evry animal can speak but dog can only bark
class Animal:
    def speak(self):
        print("every animal  can speak")

class Dog(Animal):
    def bark(self):
        print("dog only barks \n")

A1=Dog()
A1.speak()
A1.bark()

#3.parent class will be nokia which can only call child class iphon which can access both call and enternet

class Nokia:
    def call(self):
        print("only call")

class Iphone(Nokia):
    def call(self): 
        super().call() #use to acces the methode of parents class if features is same
        print("can make a call")
    def internet(self):
        print("can use internet also \n")
N1=Iphone()
N1.call()
N1.internet()

#4.the child class methode is always overide the parents class methode if both name are same this is called method overriding
#methdoe overriding
class Parent:
    def work(self):
        print("I will go to work")

class Child(Parent):
    def work(self):
        print("i will go to school")

C1=Child()
C1.work()





















