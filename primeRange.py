def check_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
        return True


n1 = 50
n2 = 100

for number in range(n1, n2 + 1):
    is_prime = check_prime(number)
    if is_prime:
        print(number)
