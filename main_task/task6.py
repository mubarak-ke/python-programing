correct_pass= "admin@123"
attempts=4
for i in range (1,5):
    pin=input("enter pin:")
    if pin==correct_pass:
        print ("Access Granted")
        break
    else:
        remaining=attempts-i
        if remaining>0:
            print("re-enter pin")
        else:
            print("blocked")
            break