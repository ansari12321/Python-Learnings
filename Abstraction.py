#abstraction-->hiding inernal details and showing only what is necessary to tha user
'''define rules
show what to do
hides how to do
uses in big problem
show only the needed ,hide the rest
'''
#Abstract class-->in this methode name is present but body is not there and the child class will complete the body
#ex
class Parent:
    def work(self):
        pass
class Child(Parent):
    def work(self):
        print("I am working")
c1=Child()
c1.work()

#Q1.
class Payment:
    def pay(self,amount):
        pass
class UPI(Payment):
    def pay(self,amount):
        print("paid using upi",amount)
U=UPI()
U.pay(15)

class card(Payment):
    def pay(self,amount):
        print("paid using cards:",amount)
c=card()
c.pay(30)

class cash(Payment):
    def pay(self,amount):
        print("paid using cash:",amount)
obj=cash()
obj.pay(20)

#create a class shape, child class circle,square and rectangle and tringle and calculate area
class Shape:
    def Drawing(self):
        print("\nDrawing started") #ready class
    def area(self):  #rule class
        pass


class circle(Shape):
    def area(self,rad):
        #self.rad=rad
        print("Circle area is :",3.14*rad*rad)
c=circle()
c.Drawing() #calling the function
c.area(2)

class square(Shape):
    def area(self,side):
        #self.side=side
        print("square area is:",side*side)
s=square()
s.Drawing()
s.area(3)

class rectangle(Shape):
    def area(self,length,breadth):
        #self.length=length
        #self.breadth=breadth
        print("reactangle area is:",length*breadth)

r=rectangle()
r.Drawing()
r.area(3,5)
class tringle(Shape):
    def area(self,base,height):
        #self.base=base
        #self.height=height
        print("tringle area is:",0.5*base*height)
t=tringle()
t.Drawing()
t.area(4,6)



#create an abstarct class name course it has two methode course info and duration then interface name exam interface it has method exam_time
#then child class which is child class of both course and exam interfacein this i have to implemnet duration ,exam type

class Course:
    def Course_info(self):
        print("\nthis is the course information")

    def duration(self):
        pass
class Exam_interface:
    def exam_time(self):
        pass

class python_course(Course,Exam_interface):
    def duration(self,month):
        self.month=month
        print("Python duration is:",self.month)
    def exam_type(self):
        print("This is practical exam")
p=python_course()
p.Course_info()
p.duration("6 months")
p.exam_type()

class java_course(Course,Exam_interface):
    def duration(self,days):
        self.days=days
        print("Java duration is:",self.days)
    def exam_type(self):
        print("this is MCQ based exam")

j=java_course()
j.Course_info()
j.duration("26 days")
j.exam_type()

class DSA_course(Course,Exam_interface):
    def duration(self,year):
        self.year=year
        print("DSA duration is:",self.year)
    def exam_type(self):
        print("this is written exam")

d=DSA_course()
d.Course_info()
d.duration("1 year")
d.exam_type()
        




































