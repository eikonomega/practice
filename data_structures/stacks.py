"""
This module implements stacks in Python.

Classes:
    SimpleStack: Stack implemented with a list.
"""


class SimpleStack:
    """Docstrings omitted for code brevity."""
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return False if self.items else True

    def size(self):
        return len(self.items)