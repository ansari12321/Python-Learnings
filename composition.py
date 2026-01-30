#composition
#One class uses another class by creating its object inside it.
#Composition is a “HAS-A” relationship where one class contains an object of another class.
class Address:
    def __init__(self,city):
        self.city=city
    def show_address(self):
        print("city:",self.city)

#student class
class student:
    def __init__(self,name,city):
        self.name=name
        #composition
        #creating object of address class inside the student class
        self.address=Address(city)
    def show_student(self):
        print("name:",self.name)

        #using object of another class

        self.address.show_address()

s=student("Kara","Delhi\n")
s.show_student()
#create a class engine then car
#car HAS-A engine create a methode start,in the car make constructo in this self passed and called engine inside the constructor,def drive inside the  car 
class Engine:
    def start(self):
        print("Engine has started")

class car:
    def __init__(self):
        self.Engine=Engine()
    def drive(self):
        self.Engine.start()
        print("Car is moving")
c=car()
#c.start()
c.drive()

#Q.-->create a teacher and subject classes where teacher HAS-A subject
