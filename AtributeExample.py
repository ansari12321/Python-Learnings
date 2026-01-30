#create a class name employee class atributes wil;l company name and object atributes will employee name and salary
class Employee:
    CompanyName="Google"
    def __init__(self,EmpName,salary):
        self.EmpName=EmpName
        self.salary=salary
E1=Employee("Karan",20000)
E2=Employee("Rahul",30000)
print(E1.EmpName,E1.salary)
print(E2.EmpName,E2.salary,"\n")
E1.EmpName="Hasan" #chnaging the E1 name and salary usinhg object atributes
E1.salary=40000
print(E1.EmpName,E1.salary) #

print(E1.CompanyName)
print(E2.CompanyName,"\n")

#next question
class Cars:
    showRooms="xyz"
    def __init__(self,model,carPrice):
        self.model=model
        self.carPrice=carPrice
c1=Cars("Venue","12lacs")
c2=Cars("Inova","39lacs")
print(c1.model,c1.carPrice)
print(c2.model,c2.carPrice)

print(c1.showRooms)
print(c2.showRooms)
