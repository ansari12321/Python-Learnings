'''class Student:
    print("this is our first class")
s1=Student()
print(s1)'''

'''class Student:
    def __init__(self):
        print("class")
s1=Student()'''
#default constructo'
'''class Student:
    def __init__(self):
        self.name="RAhul"
s1=Student()
print(s1.name)'''

#parameter constructor

class Student:
    def __init__(self,FullNAme,marks):
        self.name=FullNAme
        self.marks=marks
s1=Student("Avinash",50)
s2=Student("Rahul",55)

print(s1.name)
print(s1.marks)
print(s2.name,s2.marks)
    

