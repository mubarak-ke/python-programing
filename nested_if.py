age=int(input("enter your age: "))
if age<=0:
    print("please enter a valid age")
else:
    if age<13:
       print("you are a child.")
    elif age<18:
        print("you are a teenager.")
    else:
        print("you are an adult.")


#take input from the user
#check if the marks is between 0 and 100
# if marks is between 0 and 100 display the grades in the following categories
#90=>100 A
#80=>90  B
#70=>80   C
#60=>70 D
#50=>60 E
#below 50 fail
 
marks= float(input("Enter your Marks :"))
if (marks>=0) and (marks <=100):
    if (marks >= 90) and (marks <=100):
        grade="A"
    elif (marks >= 80) and (marks <90):
        grade = "B"
    elif (marks >= 70) and (marks <80):
        grade="c"
    elif (marks >= 60) and (marks <70):
        grade="D"
    elif(marks>=50) and(marks<60):
        grade="E"
    else:
        grade="Fail"
else:
    grade="invalid marks"

print(grade)