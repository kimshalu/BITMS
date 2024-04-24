list_=[2,4,1,-3,-5,-7,7]
negative=max(i for i in list_ if i<0)
positive=max(j for j in list_ if j%2==0)
print(negative)
print(positive)
odd=sum(k for k in list_ if k%2!=0)
print(odd)