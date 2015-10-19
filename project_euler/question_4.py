"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Brute Force Solution

"""


component_range = range(100, 10000)

palindrones = []

for component_one in component_range:
    for component_two in component_range:

        possibility = component_one * component_two

        if str(possibility) == str(possibility)[::-1]:
            palindrones.append(possibility)

palindrones.sort()
print(palindrones[-1])


import itertools

highest_palindrone = 0
for item in itertools.product(range(100, 10000), range(100, 10000)):
    possibility = item[0] * item[1]

    if str(possibility) == str(possibility)[::-1]:
        if possibility > highest_palindrone:
            highest_palindrone = possibility

print(highest_palindrone)



