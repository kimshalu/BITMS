#creating a dictionary
person_data = {"Name": "shalu kumari","age":20,"dob":"2003-11-05","Debit card number": 987654321,"PIN code": 123456,
"Height": "164cm","Tax percentage": "15.5%","Adhar card":571024535678,"Phone number":7892304911}
#printing all items in same line
print(person_data)
#printing in different line
print('Name:%s' %person_data['Name'])
print('age:%d' %person_data['age'])
print('dob:%s' %person_data['dob'])
print('Debit card number:%d' %person_data['Debit card number'])
print('PIN code:%d' %person_data['PIN code'])
print('Height:%s' %person_data['Height'])
print('Tax percentage:%s' %person_data['Tax percentage'])
print('Adhar card:%d' %person_data['Adhar card'])
print('Phone number:%d' %person_data['Phone number'])
#all values in one line
print(person_data.values())
#all key in one line
print(person_data.keys())
#all items segregatd by , and its value-pair segregated by #
for key, value in person_data.items():
    print(f"{key}#{value}", end=", ")
