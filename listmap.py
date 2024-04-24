#squaring of numbers using for
numbers=[1,2,3,4,5]
sq_num=[]
for n in numbers:
    sq_num.append(n*n)
print(sq_num)
#list comprehension
doubled_num=[num*num for num in numbers]
print(doubled_num)
#char
words='shalu'
vowels='aeiou'
res=[char for char in words if char in vowels]
print(res)
