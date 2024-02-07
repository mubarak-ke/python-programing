number1=input("enter number")
number2=input("enter number")
number3=input("enter number")

number1=float(number1)
number2=float(number2)
number3=float(number3)
if number1>number2 and number1>number3:
    print(number1," is greatest")
elif number2>number1 and number2>number3:
    print(number2,"is greatest")
else:
    print(number3," is greatest")