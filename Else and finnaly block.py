#else block
try:
    num=int(input("enter your number"))
    print(10/num)
except:
    print("error occured")
else:
    print("no error, program runs succesfully")


#finally
try:
    f=open("movieffs.txt")
except:
    print("fike not found error")
finally:
    print("program finished")
    
            
