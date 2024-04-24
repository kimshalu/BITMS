email='shalujha@gmail.com'
password=233444
uemail=str(input('enter email'))
upassword=int(input('enter password'))
if(uemail==email):
    if(upassword==password):
        print('login successful')
        otp=int(input('enter otp'))
        if(otp==1234):
            print('transaction successful')
        else:
            print('incorrect otp')
    else:
        print('login unsuccessful due to incorrect password')
else:
    print('login unsuccessful due to incorrect email')
    