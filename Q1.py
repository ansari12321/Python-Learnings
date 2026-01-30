#create a class student where total student is class atribute and increase this
#count whenever object is created
class Student:
    total_students=0
    def __init__(self,name):
        self.name=name
        Student.total_students+=1 #increasing


S1=Student("Hasan")
S2=Student("Karan")
S3=Student("Rahul")
print("Total Students",Student.total_students)
        
    
