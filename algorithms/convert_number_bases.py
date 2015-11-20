"""
This module provides functions to convert ints/decimal numbers (base 10)
to numbers of different bases.
"""

from data_structures import stacks


def binary(number):
    return convert_numeric_base(number, 2)


def octal(number):
    return convert_numeric_base(number, 8)


def hexadecimal(number):
    return convert_numeric_base(number, 16)


def convert_numeric_base(number: int, base: int) -> str:
    stack = stacks.SimpleStack()
    digits = "0123456789ABCDEF"

    while number > 0:
        stack.push(number % base)
        number //= base

    new_numeric_representation = ""
    while not stack.is_empty():
        new_numeric_representation += digits[stack.pop()]

    return new_numeric_representation


print(binary(25), bin(25))
print(octal(25), oct(25))
print(hexadecimal(25), hex(25))

print(hexadecimal(256))

