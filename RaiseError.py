#raise error-->raising your own error

age=int(input("enter ur age"))
if age<18:
    raise ValueError("Age must be 18 or above vote")
print("you can Vote")
