first_name="   muBBY  "
last_name="johnson"
email="john@mail.com "

first_name=first_name.title().strip()
last_name=last_name.title().strip()
email=email.lower().strip()
full_name=first_name+" "+last_name
print( full_name,email)

#indexing- used to get a single character from a string

#slicing- used to get multiple characters from a string
#first part is index where you want to start
#second part is the index +1 where you want to stop
print(email[-8:-5])
print(email[-8:9])
