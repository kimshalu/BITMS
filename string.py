str1='monali thakur monali thakur'
str2='ashish chuhiya'
str3='55sallu55'
print(str1.capitalize())#converts the first character into upper case letter
print(str1.casefold())#converts in lower case
#print(str1.center(8))
print(str1.count('monali thakur'))#displays number of times a single character has occured
print(str1.count('c'))
print(str1.encode())
print(str2.encode())
print(str1.endswith('r'))#prints true if given argument is same as last letter
print(str1.endswith('o'))
print(str1.expandtabs())
print(str1.find('a'))#returns the position where the value was found
print(str1.index('o'))
print(str3.isalnum())
print(str1.join(str3))#joins an elements of an iterable to the end of string
print(str1.replace('n','c'))#replaces the specified value with another value
print(str1.rsplit('o'))#splits the string
print(str1.title())
print(str1.translate('5'))




