#print(dir(locals()['__builtins__']))#double_
#exception handling
try:
    num=10
    deno=0#arithmatic error
    
    result=num/deno
    print(result)
    
except:
    print('error:denominator cannot be 0')
    
finally:
    print('executed')#by default executes whether the exception is handled or not
    
try:
    even_numbers=[2,4,6,8]
    print(even_numbers[2]/2)
    
except ZeroDivisionError:
    print('deno cannot be 0')
    
except IndexError:
    print('index out of bound')
    
#assertion error
try:
    num=int(input('enter a num:'))
    assert num%2==0#act as if
except:
    print('not a even number')
else:
    reciprocal=1/num
    print(reciprocal)
