


# # Expected usage :
#
#
# import importlib.machinery
# class CalcLoader(importlib.machinery.SourceFileLoader):
#
#     __metaclass__ = LarkMetaLoader('calc.lark', parser='lalr', transform=CalcInterpret())
#
#     def source_to_code(self, data, path='<string>'):
#         """Return the code object compiled from source.
#         The 'data' argument can be any object type that compile() supports.
#         """
#         pydata = self.interpret(data)
#         return compile(pydata, path, 'exec', dont_inherit=True)
#
#
# with palimport.importer(CalcLoader, ['.calc']):
#     from . import theanswer
#
#

# with palimport.LarkImporter(grammar='calc.lark', extensions='.calc',  parser='lalr', transform=CalcInterpret()):
#     from . import theanswer


