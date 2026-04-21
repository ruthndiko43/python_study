my_dict ={
    "name":"Ruth Komba",
    "Gender":"Female",
    "Age":"23",
    "City":"Nairobi",
    "location": {
         "postal_code": "00100",
         "town": "Kiambu"
    }
}

print(my_dict)
print(type(my_dict))

 #accessing values in a dictionary  we use keys
print(my_dict["Age"])
print(my_dict["City"])

#update and add

my_dict["Age"]=40
print(my_dict)

#adding a new property

my_dict["occupation"]="Software Developer"
print(my_dict)
print(my_dict)

#Dictionary Methods
my_dict["Hobbies"]=["swimming","reading","gaming"]
print(my_dict)
print(my_dict["Hobbies"][1])

print(my_dict["location"]["town"])

#dictionary Methods
my_dict.pop('Age')
print(my_dict)
#my_dict.popitem()
print(my_dict)
