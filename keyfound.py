d={'A':1,'B':2,'C':3}
key=input('enter key:')
if key in d.keys():
    print('key is present and the vlaue of key is:')
    print(d[key])
else:
    print('key not found')