dict1={5:'shalu',2:'sonali',3:'anjani'}
#deletes the key value
pop_key=dict1.pop(2)
print(dict1)
for x in dict1:#prints key
    print(x)
for x in dict1:
    print(dict1[x])#prints the value

for x in dict1.items():#prints the key with value in different line
    print(x)#return value is tuple
print(len(dict1))#length of dict
print(sorted(dict1))#sorts the dict in ascending and return type is list

dict1_demo=dict1.copy()#copies the dict into another dict
x=dict1_demo.pop(3)
print(x)#prints the popped element
print(dict1_demo)

print(dict1.keys())
print(dict1.values())
dict1.update({2:'sonali',3:'anju'})
print(dict1)
print(dict1.get(3))
