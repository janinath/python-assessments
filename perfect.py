num1=int(input('enter the number'))
num2=num1
sum=0
for i in range (1,num2):
    
    if num2%i==0:
        sum=sum+i
        print(sum)
    else:
        pass    
if num1==sum:
    print('it is a perfect number')
else:
    print('it is not a perfect number')    