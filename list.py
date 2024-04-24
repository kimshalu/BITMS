abc=[10,'shalu',25,'sonali']
print(abc)

for i in abc:
    print(i,end=' ')
    
print()

xyz=[25,'shalu',10,'sonali']
print(xyz)

print(abc==xyz)

a=[1,2,3,(5,6,7)]
print(a[3])

print('after changed')
abc[2]=5
print(abc)

abc[1:4]=(10,20,30)
print(abc)
