"""
This module demonstrates the time/space efficiencies of various container
types in the standard library.

"""
import sys
import timeit
import array


def iterate(test_object):
    """Iterate over a given object.  Do nothing for each iteration."""
    for item in test_object:
        pass


def membership_test(test_container):
    if 25000 in test_container:
        pass

print("\n## SPACE EFFICIENCY TESTS ##")
test_tuple = tuple(range(500000))
test_list = list(range(500000))
test_set = set(range(500000))
test_array = array.array('i', range(500000))

print("Tuple:", sys.getsizeof(test_tuple))
print("List:", sys.getsizeof(test_list))
print("Set:", sys.getsizeof(test_set))
print("Array(int):", sys.getsizeof(test_array))

print("\n## ITERATION SPEED TESTS ##")

print(
    "Tuple Iteration:",
    timeit.timeit(
        'iterate(test_tuple)',
        setup="from __main__ import iterate, test_tuple",
        number=200))

print(
    "List Iteration:",
    timeit.timeit(
        'iterate(test_list)',
        setup="from __main__ import iterate, test_list",
        number=200))

print(
    "Set Iteration:",
    timeit.timeit(
        'iterate(test_set)',
        setup="from __main__ import iterate, test_set",
        number=200))

print(
    "Array(int) Iteration:",
    timeit.timeit(
        'iterate(test_array)',
        setup="from __main__ import iterate, test_array",
        number=200))


print("\n## MEMBERSHIP SPEED TESTS ##")
print(
    "Tuple Iteration:",
    timeit.timeit(
        'membership_test(test_tuple)',
        setup="from __main__ import membership_test, test_tuple",
        number=2000))

print(
    "List Iteration:",
    timeit.timeit(
        'membership_test(test_list)',
        setup="from __main__ import membership_test, test_list",
        number=2000))

print(
    "Set Iteration:",
    timeit.timeit(
        'membership_test(test_set)',
        setup="from __main__ import membership_test, test_set",
        number=2000))

print(
    "Array(int) Iteration:",
    timeit.timeit(
        'membership_test(test_array)',
        setup="from __main__ import membership_test, test_array",
        number=2000))
