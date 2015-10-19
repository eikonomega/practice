"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def is_prime(possible_prime):
    for item in range(2, possible_prime):
        print(possible_prime, item)
        if not possible_prime % item:
            return False
    return True


primes = []
for possibility in range(2, 100):
    if is_prime(possibility):
        primes.append(possibility)

print(primes)
