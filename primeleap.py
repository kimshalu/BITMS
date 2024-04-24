list=[2004,1996,17,10,85]
def is_prime(list1):
    if num < 2:
        print(f"{num} is not a prime number.")
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            return False
    print(f"{num} is a prime number.")
    return True

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
        return True
    else:
        print(f"{year} is not a leap year.")
        return False



print("Prime numbers:")
for num in numbers:
    is_prime(num)

year = input("Enter a year to check if it's a leap year: ")
if year.isdigit():
    year = int(year)
    is_leap_year(year)
else:
    print("Please enter a valid year.")
