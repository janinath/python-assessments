# find the factorial of a number
num1=int(input('enter the number '))
num=num1
fac=1
while num>=1:
    fac=fac*num
    num=num-1
print('factorial of ',num1,' is ',fac)    