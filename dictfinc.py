def shalu():
    return "this is my bank balance"

#initializing dictionary
test_dict={"fname":shalu,"age":20,"address":"jindal"}
#printing original dict
print("the original dictionary is:"+str(test_dict))
#calling function using brakets
res=test_dict['fname']()
print("required call result:"+str(res))

#with arguments
def shalu(a,b):
    print("this is my bank balance=",a+b)

#initializing dictionary
test_dict={"fname":shalu,"age":20,"address":"jindal"}
#printing original dict
print("the original dictionary is:"+str(test_dict))
#calling function using brakets
test_dict['fname'](10,20)
