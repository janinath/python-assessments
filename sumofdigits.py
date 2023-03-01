# sum of digits

num=int(input('enter the number'))
sum=0
while num>0:
    i=num%10
    sum=sum+i
    num=num//10
print(sum)    
