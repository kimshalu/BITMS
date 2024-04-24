'''s=[]
n=int(input('enter the list size:'))
for i in range(0,n):
    e=int(input("enter the elements:"))
    s.append(e)
print(s)

print(type(s))
print(s*2)
print(len(s))
print(max(s))
print(min(s))'''
'''n=[10,25,37,40,57]
sum=0
for i in n:
    sum+=1
    print(sum)
    if i%10==7:
        print(i)'''

n=[1,2,3,4,5]
y=[]
for i in n:
    for i not in y:
        y.append(i)
        
    