"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def is_prime(possible_prime: int, known_primes) -> bool:
    """
    Attempt to divide a given number by all natural numbers between
    2 and n-1.  If any have a modolo value of 0 then it isn't a prime number.

    Args:
        possible_prime: An integer to be evaluated as a possible prime number.

    Returns:
        True if possible_prime is a prime number, otherwise False.
    """
    # for prime in known_primes:
    #     if not possible_prime % prime:
    #         return False

    for item in range(2, possible_prime):
        if not possible_prime % item:
            return False
    return True


def optimized_is_prime(possible_prime: int, known_prime_numbers: list) -> bool:
    for prime in known_prime_numbers:
        if not possible_prime % prime:
            return False
    return True


possibility = 2
primes = []
known_primes = [2]
while possibility < 2000000:
    # if is_prime(possibility, primes):
    #     primes.append(possibility)
    if optimized_is_prime(possibility, known_primes):
        known_primes.append(possibility)
    possibility += 1

print(primes)
print(sum(known_primes))