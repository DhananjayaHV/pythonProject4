#Mailing address

#solution_1
first_name = "Puneeth"
last_name= "Rajkumar"
mail_address = first_name + last_name + '@gmail.com'
print(mail_address)

# Solution_2
dictionary= { "first_name" : "Puneeth",
              "last_name": "Rajkumar",
              "formate":"@gmail.com",
              "address": "Bangalore",
              "pincode":"560001"}
print(f'Name: {dictionary["first_name"]}\nAddress: {dictionary["address"]}\nPincode: {dictionary["pincode"]}')

mail_address2 = dictionary["first_name"]+dictionary["last_name"]+dictionary["formate"]
print(mail_address2)