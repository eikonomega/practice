"""
The four adjacent digits in this 1000-digit number
that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in this 1000-digit number that
have the greatest product. What is the value of this product?
"""

# Divide the number into X segment chuncks
# Get the product of each of those chuncks
# Store the highest product

import operator
from functools import reduce

HAYSTACK = (
    "73167176531330624919225119674426574742355349194934"
    "96983520312774506326239578318016984801869478851843"
    "85861560789112949495459501737958331952853208805511"
    "12540698747158523863050715693290963295227443043557"
    "66896648950445244523161731856403098711121722383113"
    "62229893423380308135336276614282806444486645238749"
    "30358907296290491560440772390713810515859307960866"
    "70172427121883998797908792274921901699720888093776"
    "65727333001053367881220235421809751254540594752243"
    "52584907711670556013604839586446706324415722155397"
    "53697817977846174064955149290862569321978468622482"
    "83972241375657056057490261407972968652414535100474"
    "82166370484403199890008895243450658541227588666881"
    "16427171479924442928230863465674813919123162824586"
    "17866458359124566529476545682848912883142607690042"
    "24219022671055626321111109370544217506941658960408"
    "07198403850962455444362981230987879927244284909188"
    "84580156166097919133875499200524063689912560717606"
    "05886116467109405077541002256983155200055935729725"
    "71636269561882670428252483600823257530420752963450")


def brute_force_highest_product_search(segment_length: int) -> int:
    """
    O(n)

    Args:
        segment_length: An int specifying the length of segments to
            consider the products of.

    Returns:
        An int representing the largest product of all considerate
        segments.
    """
    highest_product = 0
    for index, value in enumerate(HAYSTACK):
        segment = [
            int(number) for number in (HAYSTACK[index:index + segment_length])]
        product = reduce(operator.mul, segment, 1)
        if highest_product < product:
            highest_product = product

    return highest_product


def highest_product_search(segment_length: int) -> int:
    """
    Same functionality but with a couple of optimizations:
        - Don't calculate the product if a 0 is in the segment.

    Args:
        segment_length: An int specifying the length of segments to
            consider the products of.

    Returns:
        An int representing the largest product of all considerate
        segments.
    """
    highest_product = 0
    for index, value in enumerate(HAYSTACK):

        segment = [
            int(number) for number in (HAYSTACK[index:index + segment_length])]

        # Optimization: Don't calculate product if 0 in segment.
        if 0 in segment:
            continue

        product = reduce(operator.mul, segment, 1)
        if highest_product < product:
            highest_product = product

    return highest_product


if __name__ == '__main__':
    import timeit
    print(brute_force_highest_product_search(13))
    print(highest_product_search(13))

    print(timeit.repeat("brute_force_highest_product_search(13)",
                        setup="from __main__ import brute_force_highest_product_search",
                        number=100, repeat=3))

    print(timeit.repeat("highest_product_search(13)",
                        setup="from __main__ import highest_product_search",
                        number=100, repeat=3))
