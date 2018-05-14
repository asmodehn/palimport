

import filefinder2.machinery
import palimport.lark


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


class CalcLoader(palimport.lark.LarkLoader):

    grammar = """
//
// Simple calculator grammar
//

?start: sum
      | NAME "=" sum    -> assign_var

?sum: product
    | sum "+" product   -> add
    | sum "-" product   -> sub

?product: atom
    | product "*" atom  -> mul
    | product "/" atom  -> div

?atom: NUMBER           -> number
     | "-" atom         -> neg
     | NAME             -> var
     | "(" sum ")"

%import common.CNAME -> NAME
%import common.NUMBER
%import common.WS_INLINE

%ignore WS_INLINE

"""
    parser = 'lalr'

    transformer = CalculateTree()



with palimport.lark.importer(CalcLoader, ['.calc']):
    try:
        from . import theanswer
    except SystemError:
        import theanswer


# to be able to test basic parsing functionality
if __name__ == '__main__':
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        print(calc.parse(s).pretty())

