#create dict
emp={'name':'shalu','age':20,'sal':500,'dob':'5 nov 2003'}
print(emp)
print(type(emp))

dict={}
print(dict)#prints empty dict

'''dict1=dict([(2,'shalu'),(3,'sonali')])#tuple is used to make dictionary
print(dict1)'''

emp={'name':'shalu','age':20,'sal':500,'dob':'5 nov 2003'}
print(type(emp))
print('name:%s' %emp['name'])#prints in single
print('age:%d' %emp['age'])
print('sal:%d' %emp['sal'])
print('dob:%s' %emp['dob'])

dict[0]='sonam'
dict[1]='samya'
print(dict)
dict['emp_age']=18,19#takes it as tuple by default without bracket
print(dict)
# taking input
emp['name']=input('name:')
emp['age']=int(input('age:'))
emp['sal']=int(input('sal:'))
emp['dob']=input('dob:')
print('new data:\n')
print(emp)
#deleting
del emp['name']
print (emp)
del emp #deletes the full dict
print(emp)#shows error emp is not defined
