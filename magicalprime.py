def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def rev_number(n):
    return int(str(n)[::-1])

def magicalprime(n):
    if prime(n):
        reversed_n = rev_number(n)
        return prime(reversed_n)
    return False

num = int(input("Enter a number: "))
if magicalprime(num):
    print(num, "is a magical prime.")
else:
    print(num, "is not a magical prime.")



