#example on raise error 1
#age=int(input("enter ur age: "))

#if age<18:
   # raise ValueError("age must be 18 or more")
#print("you are eligible")

#ex2
num=int(input("enter ur number: "))
#if number is negative , we manually raise an error
#python does not automatically trest negative number as wrong
if num<0:
    raise ValueError("number must be positive")

#this will run if no exception ocuure
print("you entered: ",num)
    
