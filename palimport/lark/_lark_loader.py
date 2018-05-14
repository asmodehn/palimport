
import filefinder2
import logging
import tempfile
import os
import six

from lark import Lark
from._utils import _verbose_message

from ._lark_metaloader import LarkMetaLoader


@six.add_metaclass(LarkMetaLoader)
class LarkLoader(filefinder2.machinery.SourceFileLoader):
    """
    Loader for a sourcefile, where the parser is Lark
    """

    def get_code(self, fullname):
        source = self.get_source(fullname)
        _verbose_message('parsing code for "{0}"'.format(fullname))
        try:
            ast = self.source_to_ast(source, self.get_filename(fullname))
            _verbose_message('compiling code for "{0}"'.format(fullname))
            code = self.ast_to_code(ast, self.get_filename(fullname))
            return code
        except TypeError:
            raise

    def source_to_code(self, data, path):
        """Return the code object compiled from source.
        The 'data' argument can be any object type that compile() supports.
        """
        return compile(data, path, 'exec', dont_inherit=True)

    def source_to_ast(self, data, path):
        _verbose_message('parsing code in "{0}"'.format(path))
        return self.lark.parse(data)

    def ast_to_code(self, ast, path):
        pysource = interpret(ast)
        return self.source_to_code(pysource, path)