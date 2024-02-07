days=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
print(days[2]) #display wednesday
print(len(days))#length of daysg
#conv into a list
my_list=list(days)
#update
my_list[3]="thur"
print(my_list)
#convert it back to a tuple
my_list=tuple(my_list)
print(my_list)