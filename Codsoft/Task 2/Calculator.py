print("******* CALCULATOR *******")

while(True):
    a=int(input("\nEnter 1st Number: "))
    b=int(input("Enter 2nd Number: "))
    print('''\nChoose The Following Operation:
          1.Addition
          2.Subtraction
          3.Multiplication
          4.Division
          5.Remainder
          6.Exit''')
    choice=int(input("\nEnter your choice: "))

    if(choice==1):
        result=a+b
        print("\nResult is: ",result)
        break;
    elif(choice==2):
        result=a-b
        print("\nResult is: ",result)
        break;
    elif(choice==3):
        result=a*b
        print("\nResult is: ",result)
        break;
    elif(choice==4):
        result=a/b
        print("\nResult is: ",result)
        break;
    elif(choice==5):
        result=a%b
        print("\nResult is: ",result)
        break;
    elif(choice==6):
        break;
    else:
        print("\nInvalid choice\nEnter again!\n")