import palimport._lark


with palimport._lark.Importer():
    if __package__ is None:
        import calc
    else:  # attempting relative import when possible
        from . import calc


# # to be able to test basic parsing functionality
if __name__ == '__main__':
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        print(calc.parser.parse(s).pretty())
