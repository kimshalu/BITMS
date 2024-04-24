# union(or)
d1={'mon','tue','wed','thur','sun'}
d2={'fri','sat','sun'}
print(d1.union(d2))#no dublication
#print(d1|d2)
s1={1,2,3}
s2={2,3,4}
s3={3,4,5}
common_elements=s1.union(s2,s3)#no dublication
print(common_elements)
#intersection(and)
print(s1.intersection(s2,s3))
print(d1.intersection(d2))
#print(d1&d2)
#difference(-)
print(d1-d2)
print(s1-s2)
print(s1.difference(s2))
#symmetric_difference(^)
a={1,2,3,4,5,6}
b={1,2,9,8,10}
c=a^b
print(c)
d=a.symmetric_difference(b)#displays elements from both set
print(d)
#comparition
print(d1>d2)
print(d1<d2)
print(d1==d2)
x={1,2,3,5,4}
y={1,2,3}
print(x>y)#x is subset of y soo true
