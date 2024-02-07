total_stock=0
prods = [['omo','30kshs','300'], ['milk','50kshs','200'],['bread','45kshs','359'], ['coffee','5kshs','79'],['tea','100ksh','1000']]
for i in prods:
# extract and convert into interger
    stock=int(i[2])
#update total stock
    total_stock=total_stock+stock
#print total stock
print(total_stock)
#938