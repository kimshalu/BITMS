class A():
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



class B(A):
    def neon(n):
        square = n * n
        digit_sum = sum(int(digit) for digit in str(square))
    return digit_sum == n

n = int(input("Enter a number: "))
if neon(n):
    print(n, "is a neon number.")
else:
    print(n, "is not a neon number.")

class C(A):
 name = "Shalu"

for i in range(len(name)):
    for j in range(len(name)):
        if i == j or i + j == len(name) - 1:
            print(name[i], end="")
        else:
            print(" ", end="")
    print()   

class D(A):
    a=input('enter the a value')
    rev=(str(a[::-1]))
    print(rev)
    
class E(B,C):
    dictt={"shalujha6044@gmail.com":"5789234","abcd@gmail.com":"123456","xyz@gmail.com":"098765"}
otp=1234
user_email = input("Enter your email: ")
user_pass = input("Enter your password: ")
if user_email in dictt:
    if user_pass == dictt[user_email]:
            print("Login successful.")
            user_otp = int(input("Enter OTP: "))
            if user_otp==otp:
                print("Logged in to your account.")
            else:
                print("Invalid OTP.\nLogin unsuccessful.")
                exit()
    else:
        print("password not found.\nLogin unsuccessful.")
        exit()
else:    
    print("Email not found.\nLogin unsuccessful.")
    exit()


def withdraw(account, amount, otp):
    if otp == otp:
        if amount > account['balance']:
            print("Insufficient funds!")
        else:
            account['balance'] -= amount
            account['transactions'].append(f"Withdrawal: ${amount}")
            print(f"Withdrawal successful. Remaining balance: ${account['balance']}")
    else:
        print("Invalid OTP. Withdrawal unsuccessful.")
        
def deposit(account, amount, otp):
    if otp == otp:
        account['balance'] += amount
        account['transactions'].append(f"Deposit: ${amount}")
        print(f"Deposit successful. Remaining balance: ${account['balance']}")
    else:
        print("Invalid OTP. Deposit unsuccessful.")

def get_balance(account):
    return account['balance']

def get_transaction_history(account):
    return account['transactions']
    print('count='+transcations.count('transactions'))

account = {
    'balance': 1000,
    'transactions': []
}

choices = {
    '1': deposit,
    '2': withdraw,
    '3': get_balance,
    '4': get_transaction_history
}

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '5':
        print("Exiting program.")
        break

    if choice in choices:
        if choice == '1' or choice == '2':
            if choice== '4':
                if count==5:
                    print('transcation limited reached')
            amount = float(input("Enter amount: "))
            user_otp = int(input("Enter OTP: "))
            choices[choice](account, amount, user_otp)
        else:
            print(choices[choice](account))
    else:
        print("Invalid choice. Please try again.")

ob=E()
ob1=D()
ob.deposit()
ob.withdraw()

