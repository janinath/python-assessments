 # input the numbers 
a=int(input('enter the first number'))
b=int(input('enter the second number'))

 # find the largest and smallest numbers ( largest = f  and  smallest = l )
if a<b:
    f=b
    l=a
else:
    f=a    
    l=b

 # checking whether the numbers are positive or not
if f>=1 and l>=1:

#finding the hcf value   
    while f%l !=0:
        c=f%l
        d=l%c
        f=l
        l=c
    # hcf=l 
print('the hcf is ',l)    