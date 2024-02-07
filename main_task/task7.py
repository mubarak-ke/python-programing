marks=float(input("enter marks: "))
if (marks>=0) and (marks<=100):
    if (marks>=79):
        print("A")
    elif(marks>=60) and  (marks<79):
        print("B")
    elif(marks>=59) and (marks<49):
        print("C")
    elif(marks>=40) and (marks<49):
        print("D")
    else:
        print("F")
else:
    print("Invalid Marks")