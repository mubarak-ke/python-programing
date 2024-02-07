num1=float(input("enter number"))
num2=float(input("enter number"))
num3=float(input("enter number"))
num4=float(input("enter number"))
if num1>num2 and num1>num3 and num1>num4:
    result=f"the  largest number is {num1}"
elif num2>num1 and num2>num3 and num2>num4:
    result=f" the largest number is {num2}"
elif num3>num1 and num3>num2 and num3>num4:
    result=f"the largest number is {num3}"
else:
    result=f"the largest number is{num4}"
    print(result)