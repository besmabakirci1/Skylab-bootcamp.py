from math import *
num1=float(input("Please enter the first number:"))
num2=float(input("Please enter the second number:"))
Process=input("Please enter the operation (+,-,/,*,**):")

if Process == "+":
    result = num1 + num2
    print(f"result:{result}")

elif Process == "-":
    result = num1 - num2
    print(f"result:{result}")

elif Process == "/":
    if(num2)!= 0: 
        result = num1 / num2
        print(f"result:{result}")
    else:
        print("Error: Division by zero!")

elif Process == "*":
    result = num1 * num2
    print(f"result:{result}")

elif Process == "**":
    result = num1**num2
    print(f"result: {result}")
else:
    print("Invalid operation. Please try again.")




     
