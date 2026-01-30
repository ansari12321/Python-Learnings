#attributes
#1 Class Atributes
#2 object Atributes

class Student:
    collegName="lpu"
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
s1=Student("Hasan",70)
s2=Student("Rahul",60)

print(s1.name,s1.marks) #object atributes
print(s2.name,s2.marks)#object atributes
print(s1.collegName) #class atributes
print(s2.collegName) #class atributes
print(Student.collegName) #print using class name
#s1.collegName="Du"  if we run this code will give output firs becz object atributes will overWrite the class atributres

Student.collegName="DU" #updating the college name using class
print(s1.collegName)  
print(s2.collegName)
