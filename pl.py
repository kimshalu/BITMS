list=[2004,1996,17,10,85]
def is_prime(list):
    if num <= 1:
        
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            flag=1
    if(flag==1):
        print('prime number')
    else:
        print('not a prime number')

def is_leap_year(list):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

is_prime(list)
is_leap_year(list)