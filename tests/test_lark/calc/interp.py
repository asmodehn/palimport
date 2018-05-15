import os
import palimport.lark
from lark import InlineTransformer


# class CalculateTree(InlineTransformer):
#     from operator import add, sub, mul, truediv as div, neg
#     number = float
#
#     def __init__(self):
#         self.vars = {}
#
#     def assign_var(self, name, value):
#         self.vars[name] = value
#         return value
#
#     def var(self, name):
#         return self.vars[name]



with palimport.lark.importer(palimport.lark.LarkGrammarLoader, ['.lark']):
    if __package__ is None:
        import calc
    else:  # attempting relative import when possible
        from . import calc



class CalculatePython(InlineTransformer):
    from operator import add, sub, mul, truediv as div, neg
    number = float

    def __init__(self):
        pass

    def assign_var(self, name, value):
        # translate to python code instead of direct evaluation
        return "{name} = {value}".format(**locals())

    def var(self, name):
        # translate to python code instead of direct evaluation
        return "{name}".format(**locals())


class CalcLoader(palimport.lark.LarkLoader):
    """
    Custom Loader, loading a custom AST into python code.
    """
    parser = calc.parser
    transformer = CalculatePython()


with palimport.lark.importer(CalcLoader, ['.calc']):
    try:
        from . import theanswer
    except SystemError:
        import theanswer

assert theanswer.ANSWER == 42

# to be able to test basic interpreting functionality
if __name__ == '__main__':
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        AST = calc.parser.parse(s)
        pycode = CalculatePython().transform(AST)
        # TODO : fix that in the grammar
        if not isinstance(pycode, (str,)):
            pycode = str(pycode)
        print(eval(pycode, {"__builtins__": None}, {}))
        print(exec(pycode, {"__builtins__": None}, {}))

