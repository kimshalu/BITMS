l_ist=[1,2,3,-1,-2,5,8]
print(l_ist)
sum=0
e=0
o=0
for i in l_ist:
    if i<0:
        sum+=i
    elif i%2==0 and i>0:
        e+=i
    else:
        o+=i
print('sum of negative no:',sum)
print('sum of positine even no:',e)
print('sum of positive odd no:',o)   