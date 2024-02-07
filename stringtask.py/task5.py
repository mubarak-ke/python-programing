r='["E","W","C"]'
# r="".join(filter(str.isalpha,r))
r=r.replace("[","").replace("]","").replace('"',"").replace(",","")
print(r)
