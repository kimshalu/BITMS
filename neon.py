def neon(n):
    square = n * n
    digit_sum = sum(int(digit) for digit in str(square))
    return digit_sum == n

n = int(input("Enter a number: "))
if neon(n):
    print(n, "is a neon number.")
else:
    print(n, "is not a neon number.")
