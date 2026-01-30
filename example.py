#ex1
def test():
    try:
        return 10
    finally:
        return 20
print(test())

#example2 seprate code
try:
    try:
        x=int("abc")
    except ValueError:
        print("inner handled")
        raise
except Exception:
    print("outer hnadled")

#ex3 seprate code important-->only finally block can over write the try block
def test():
    try:
        return 10
    except:
        return 20
    else:
        return 30
print(test())
