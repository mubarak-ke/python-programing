# numbers=list(range(0,10))
# for i in numbers:
#     if i==6:
#         print(f"{i} available")
#         break
#     else:
#         print(f"{i} not available")

correct_pin=1234
attempts=3

for i in range(1,4):
    pin=int(input("Enter  PIN: "))
    if pin==correct_pin:
        print("access granted")
        break
    else:
        remaining=attempts-i
        if remaining>0:
            print("re-enter the pain")
        else:
            print("blocked")