import os
from lark import Lark, InlineTransformer

# TODO : lark grammar importer
# __path__ = os.path.dirname(__file__)
#
# with open(os.path.join(__path__, "calc.lark")) as f:
#     calc_parser = Lark(f, parser='lalr')

import lark_import

with lark_import.importer():  #parser='lalr'):
    from . import calc


def main():
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        print(calc.parse(s).pretty())


# to be able to test basic parsing functionality
if __name__ == '__main__':
    main()

