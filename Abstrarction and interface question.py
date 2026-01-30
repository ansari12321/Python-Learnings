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
        
