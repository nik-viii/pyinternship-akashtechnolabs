n = int(input("Enter the integer: "))
if(n < 100):
    if(n % 2 == 0):
        print(str(n)+" is even.")
    else:
        print(str(n)+" is odd.")
else:
    print("Number is not less than 100.")
