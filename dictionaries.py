person = {
    "name" : "John Doe",
     "age":30,
    "location": "Nairobi",
     "email" :"johndoe@mail.com"
}
#accessing values in a dictionary we use keys 
print(person["name"]) 
print(person["location"])
print(person["age"]) 
print(person["email"]) 
print(person)  

#adding key value pairs polling station,occupation

person["city"]="New york"
print(person)
#modify/update to kilifi
person["age"]=40
person["location"]="Kilifi"
#display all keys
print(person.keys())
print(person.values())
print(person.items())

#check if a key exists in the dictionary using 'in' keyword
