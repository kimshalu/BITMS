class Mango:
    def _init_(self):#acts as a constructor in python
        print("this is what")
    def shalu(self):
        print('this is without parameter')
    def sonali(self,a,b):
        print(a+b,'this is with parameter')
    def magicalprime(self,a):
        flag=0
        for i in range(2,a):
            if a%i==0:
                flag=1
        if(flag==1):
            rev=(str(a[::-1]))
            if rev%i==0:
                print(f'{a} is not a magicalprime number')
            else:
                print(f'{a} is a magicalprime number')
                
    
    def neon(self,a):
        print('check neon or not')
        
m=Mango()
m.shalu()
m.sonali(10,20)
m.magicalprime('101')
m.neon(7)