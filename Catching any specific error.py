try:
    num=int(input("enter a number"))
    print(100/num)
except ZeroDivisionError:
    print("you cannot devide any number by zero")
except ValueError:
    print("enter only number")
