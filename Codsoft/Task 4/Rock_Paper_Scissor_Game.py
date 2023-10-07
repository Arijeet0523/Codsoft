import random

a=random.randint(1,3);
if(a==1):
    comp='r'
elif(a==2):
    comp='p'
else:
    comp='s'
    
def gameWin(comp,you):
    if(comp==you):
        return 0;
    if(comp=='s' and you=='r'):
        return 1;
    elif(comp=='s' and you=='p'):
        return -1;
    if(comp=='p' and you=='s'):
        return 1;
    elif(comp=='p' and you=='r'):
        return -1;
    if(comp=='r' and you=='p'):
        return 1;
    elif(comp=='r' and you=='s'):
        return -1;
    
        
print("************\tRock Paper Scissor\t************\n")
while(True):
    you=input("Enter your choice: \nRock(r)\tPaper(p)\tScissor(s)\n")
    if(you=='r' or you=='p' or you=='s'):
        break;
    else:
        print("\nInvalid Input\nPlease Enter Again :)\n")


print("\nComp Chose: ",comp)
print("You Chose:",you,"\n")

g=gameWin(comp,you)

if(g==0):
    print("Draw")
elif(g==1):
    print("You Won!")
else:
    print("You Lose!")