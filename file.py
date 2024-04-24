fileptr=open('shaluk.txt','r')#reads the file
fileptr2=open('shaluk.txt','r')

if fileptr:
    print('opened')
else:
    print('file not found')
fileptr1=open('shaluk.txt','w')#writes the file
fileptr1.write('yashitha')
print(fileptr1)

fileptr2=open('shaluk.txt','a')#appends the file
fileptr2.write('\n yashitha')
print(fileptr2)
print(fileptr.read(10))#reads  
fileptr.close()

