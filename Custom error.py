#custom Error
class LowBalanceError(Exception):
    #this line create a custom exception named as LowBalanceError
    #pass is used because class cannnot be empty in python
    #we dont need to add any logic inside the claSS RIGHT NOW

    pass

balance=500
withdraw=int(input("enter amount"))
if withdraw>balance:
    raise LowBalanceError("Insufficient balance")
print("withdraw succesfull")
