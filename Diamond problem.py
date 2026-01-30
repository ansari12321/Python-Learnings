'''1.Diamond problem

class A:
    print("class A")






class B(A):
    print("class B")


class C(A):
    print("class C")



class D(B,C):
    pass
    
d1=D()
'''
#2.

class A:
    def message(self):
        print("this is message from class A")
class B(A):
    def message(self):
        print("this is message from class B")
class C(A):
    def message(self):
        print("this is message from class C")

class D(B,C):
    
    pass
obj=D()
obj.message()



