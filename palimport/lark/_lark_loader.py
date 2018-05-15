
import filefinder2
import logging
import tempfile
import os
import six

from lark import Lark
from._utils import _verbose_message

from ._lark_metaloader import LarkMetaLoader




class LarkGrammarLoader(filefinder2.machinery.SourceFileLoader):

    # TODO : investigate : removing get_code breaks loader !!!
    def get_code(self, fullname):
        try:
            source = self.get_source(fullname)
        except Exception:
            print("get_code Exception")
            raise
        _verbose_message('compiling code for "{0}"'.format(fullname))
        try:
            code = self.source_to_code(source, self.get_filename(fullname))
            return code
        except TypeError:
            raise

    def get_source(self, name):
        """Implementing actual python code from file content"""
        path = self.get_filename(name)

        # Returns decoded string from source file
        larkstr = super(LarkGrammarLoader, self).get_source(name)
        larkstr = "from lark import Lark; parser = Lark(\"\"\"{larkstr}\"\"\", parser='lalr')""".format(**locals())

        return larkstr


@six.add_metaclass(LarkMetaLoader)
class LarkLoader(filefinder2.machinery.SourceFileLoader):
    """
    Loader for a sourcefile, where the parser is Lark
    """

    parser = None  # mandatory class member. Need to be defined by any derived class
    transformer = None  # mandatory class member. Need to be defined by any derived class

    # def get_code(self, fullname):
    #     source = self.get_source(fullname)
    #     _verbose_message('parsing code for "{0}"'.format(fullname))
    #     try:
    #         ast = self.source_to_ast(source, self.get_filename(fullname))
    #         _verbose_message('compiling code for "{0}"'.format(fullname))
    #         code = self.ast_to_code(ast, self.get_filename(fullname))
    #         return code
    #     except TypeError:
    #         raise

    # We avoid overriding get_source here to not have to deal with decode_source() if we can avoid it

    def get_code(self, fullname):
        try:
            source = self.get_source(fullname)
        except Exception:
            print("LarkLoader get_code Exception")
            raise

        _verbose_message('transforming code for "{0}"'.format(fullname))

        transformed_source = self.transformer.transform(self.parser.parse(source))

        _verbose_message('compiling code for "{0}"'.format(fullname))
        try:
            code = self.source_to_code(transformed_source, self.get_filename(fullname))
            return code
        except TypeError:
            raise

    def source_to_code(self, data, path):
        """Return the code object compiled from source.
        The 'data' argument can be any object type that compile() supports.
        """
        return compile(data, path, 'exec', dont_inherit=True)

    # def source_to_ast(self, data, path):
    #     _verbose_message('parsing code in "{0}"'.format(path))
    #     return self.lark.parse(data)
    #
    # def ast_to_code(self, ast, path):
    #     pysource = interpret(ast)
    #     return self.source_to_code(pysource, path)