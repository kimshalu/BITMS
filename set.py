states={'goa','delhi','bihar'}
#states=set(['goa','delhi','bihar'])
print(states)
for i in states:
    print(i)
print(type(states))
#dictionary and set
set1={ }
set2={1,}
print(type(set1))
print(type(set2))
#add 
districts=set(['ooty','mangalore','darjelling','manali'])
print(districts)
districts.add('shimla')
print(districts)
#elements added via update
districts.update(['kanyakumari','madurai'])
print(districts)
#discard
districts.discard('ooty')
print(districts)
#districts.discard('vijayawada')#no error
print(districts)
#remove
districts.remove('manali')
print(districts)
#sdistricts.remove('vijayawada')#error 
print(districts)
#pop
districts.pop()
print(districts)

#clear
districts.clear()
print(districts)#full element is popped out

