correct_email = "admin@mail.com"
correct_password = "Admin@123"

attempts=3

for i in range(1,4):
    email=input(("enter email: "))
    password=input(("Enter password: "))
    if correct_email==email and correct_password==password:
        print("login successful")
    else:
       remaining=attempts-i
    if remaining>0:
            print("re-enter pin")
    else:
            print("blocked")
            break 
    print("invalid username or password")
