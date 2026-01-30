#create a class stutdent show name is the normal methode and static methode show college name
class Student:
    college_name="LPU"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        


        
    def Showname(self):
        print(self.name)

    @staticmethod
    def Showcollege():
        print(Student.college_name)
s1=Student("Rahul",54)

s1.Showname()
Student.Showcollege()
        
