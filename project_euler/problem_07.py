"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10,001st prime number?
"""


# Brute Force - n^2 I think
def is_prime(possible_prime: int) -> bool:
    """
    Attempt to divide a given number by all natural numbers between
    2 and n-1.  If any have a modolo value of 0 then it isn't a prime number.

    Args:
        possible_prime: An integer to be evaluated as a possible prime number.

    Returns:
        True if possible_prime is a prime number, otherwise False.
    """
    for item in range(2, possible_prime):
        if not possible_prime % item:
            return False
    return True

possibility = 2
primes = list()
while len(primes) < 10001:
    if is_prime(possibility):
        primes.append(possibility)
    possibility += 1

print(primes[-1])

