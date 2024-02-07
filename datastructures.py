my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]
print(my_ds[3][2]["currency"])

print(my_ds[2])

#print math
print(my_ds[3][1])
#add amount in the dictionary
my_ds[3][2]["amount"]=90
print(my_ds)

my_ds[4]=str(my_ds[4])#convert to a string
my_ds[4]=my_ds[4][::-1]#update
#convert back to integer
my_ds[4]=int(my_ds[4])
print(my_ds)

#convert it int alist
my_ds[5]=list(my_ds[5])
#update john to jane
my_ds[5][1]="Jane"
#convert it back to a tuple
my_ds[5]=tuple(my_ds[5])
print(my_ds)




# input
string = str(input())

# output
print(string)

# Or by default
string_default = input()

# output
print(string_default)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          