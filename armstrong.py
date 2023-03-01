 # input the numbers
num=(input('enter the number'))

 # find the length
no=int(len(num))
 
num2=int(num)
num1=int(num)
rem=0
 #finding the armstrong numbers
while num1 >=1:
   rem=rem +( (num1%10)**no)
   num1=num1//10

if num2==rem:
    print('it is an armstrong number ')
else:
    print('it is not an armstrong number')