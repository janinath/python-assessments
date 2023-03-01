 #input the word
word=input('enter the word ')
 
 #reverse the word
reverse=word[::-1]

 #checking palindrom
if word==reverse:
    print('it is a palindrom')
else:
    print('it is not a palindrom')    