try:
    try:
        print(1/0)
    finally:
            print("inner finaaly")
except ZeroDivisionError:
    print("outer exception")
finally:
    print("outer finally")
