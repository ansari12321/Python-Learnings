#move all zeros at the end
num =[0,1,0,3,12]
count_zeros=num.count(0)
n1=[x for x in num if x!=0]
n2=[0]*count_zeros
print(n1+n2)
