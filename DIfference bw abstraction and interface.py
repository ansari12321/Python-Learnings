#when we remove the ready class methdoe from the abstraction class then it becomes interface
#by abstraction
class Payment:
    def Started(self):
        print("Payment started")
    def pay(self,amount):
        pass
class UPI(Payment):
    def pay(self,amount):
        print("Done By UPI:",amount)
class Card(Payment):
    def pay(self,amount):
        print("DOne BY Card:",amount)

U=UPI()
U.Started()
U.pay(1000)

C=Card()
C.Started()
C.pay(1500)

#by interface
class Payment:
    #def Started(self):
        #print("Payment started")
    def pay(self,amount):
        pass
class UPI(Payment):
    def pay(self,amount):
        print("\nDone By UPI:",amount)
class Card(Payment):
    def pay(self,amount):
        print("DOne BY Card:",amount)
U=UPI()
U.pay(1000)

C=Card()
C.pay(1500)
