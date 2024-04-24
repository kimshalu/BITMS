def countdict(s):
   
    count={}
    words=s.split()
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    return count

s=input('enter the string value:\n')
dictt=countdict(s)
print(count)

            