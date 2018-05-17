
import palimport.lark


from lark import InlineTransformer



with palimport.lark.importer(palimport.lark.LarkGrammarLoader, ['.lark']):
    if __package__ is None:
        import calc
    else:  # attempting relative import when possible
        from . import calc




def test_parse():

        with palimport.lark.importer(CalcLoader(calc.lark), ['.calc']):
            try:
                from . import theanswer
            except SystemError:
                import theanswer

        assert theanswer.ANSWER == 42


# # to be able to test basic parsing functionality
if __name__ == '__main__':
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        print(calc.parser.parse(s).pretty())
