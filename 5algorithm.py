def prime_number(number):
    isPrime = True
    for n in range(2,number):
        if (number % n == 0):
            isPrime = False
            break
    return isPrime


# for x in range(2, 100):
#     if (prime_number(x)):
#         print(x)

# print(prime_number(11))


def is_prime(n):
    if n <= 1:
        return False

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    print("sqt root: ",math.sqrt(n))

    for i in range(2, int(math.sqrt(n)) + 1):
        print("i: ", i)
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                print("j: ", j)
                sieve[j] = False
    print("sieve: ",sieve)

    return sieve[n]


import math
print(is_prime(10))

