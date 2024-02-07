marks=float(input("enter marks"))
if (marks>=0) and(marks<=100):
    if(marks>=90) :
        grade="A"
    elif(marks>=80)and(marks<89):
        grade="B"
    elif(marks>=70)and(marks<79):
        grade="C"
    elif(marks>=60)and(marks<69):
        grade="D"
    
    else:
        grade=" F"    
else:
      grade="invalid marks"
print(grade)


# number 2
num1=float(input("enter number"))
num2=float(input("enter number"))
if num1>0 and num2>0:
    result="positive"
    sum_of_numbers=num1+num2
    if sum_of_numbers%2==0:
        result="is even",sum_of_numbers

    else:
        result="is odd",sum_of_numbers
else:
    result="negative numbers"
print(result)

# # number 3
# time_24_hour = input("Enter the time in 24-hour format (Hr:Min): ")


# hours, minutes = map(int, time_24_hour.split(':'))
# # Check if the input is valid
# if 0 <= hours < 24 and 0 <= minutes < 60: