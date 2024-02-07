phone_number=input("enter number")

if phone_number[0:4]==("+254") and len(phone_number)==13:
 print ("valid number")
elif phone_number[0:2]==("07"or"01") and len(phone_number)==10:
    print("+254"+ " "+phone_number[1:])
elif phone_number[0]==("7")and len(phone_number)==9:
   print("+254"+phone_number)
elif phone_number[0:3]==("254")and len(phone_number)==12:
   print("+"+ phone_number)
else:
   print("invalid number")
n
