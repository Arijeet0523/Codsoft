import random
import string

length=int(input("Enter the length of your password: "))

print('''Chose Charachter set for your password from the following:
      1.Digits
      2.Letters
      3.Special Characters
      4.Exit ''')

characterset=""

while(True):
    choice=int(input("Enter Your Choice: "))
    if(choice==1):
        characterset+=string.digits
    elif(choice==2):
        characterset+=string.ascii_letters
    elif(choice==3):
        characterset+=string.punctuation
    elif(choice==4):
        break;
    else:
        print("Invalid Operation !")
        
password=[]

for i in range(length):
    randchar=random.choice(characterset)
    password.append(randchar)
    
print("The Generated Password is :","".join(password))

