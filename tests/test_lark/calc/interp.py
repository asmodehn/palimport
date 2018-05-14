import os
from palimport import lark
from lark import InlineTransformer


class CalculateTree(InlineTransformer):
    from operator import add, sub, mul, truediv as div, neg
    number = float

    def __init__(self):
        self.vars = {}

    def assign_var(self, name, value):
        self.vars[name] = value
        return value

    def var(self, name):
        return self.vars[name]


with lark.importer(parser='lalr', transformer=CalculateTree()):
    from . import calc

# to be able to test basic parsing functionality
if __name__ == '__main__':
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        print(calc(s))

