import filefinder2
import logging
import tempfile
import os

from lark import Lark
from._utils import _verbose_message


class LarkLoader(filefinder2.machinery.SourceFileLoader):
    """
    Python Loader for Lark files.
    """

    def __init__(self, fullname, path):

        self.logger = logging.getLogger(__name__)
        # to normalize input
        path = os.path.normpath(path)

        # relying on usual source file loader since we have generated normal python code
        super(LarkLoader, self).__init__(fullname, path)

    def __repr__(self):
        return "LarkLoader/{0}({1}, {2})".format(".lark", self.name, self.path)

    def get_source(self, name):
        """Implementing actual python code from file content"""
        path = self.get_filename(name)

        # Returns decoded string from source file
        larkstr = super(LarkLoader, self).get_source(name)

        larkstr = "from lark import Lark; parser = Lark(\"\"\"{larkstr}\"\"\", parser='lalr')""".format(**locals())

        return larkstr

    def source_to_code(self, data, path):
        """Return the code object compiled from source.
        The 'data' argument can be any object type that compile() supports.
        """
        return compile(data, path, 'exec', dont_inherit=True)

    def get_code(self, fullname):
        source = self.get_source(fullname)
        _verbose_message('compiling code for "{0}"'.format(fullname))
        try:
            code = self.source_to_code(source, self.get_filename(fullname))
            return code
        except TypeError:
            raise

    # Useful ??
    # @staticmethod
    # def get_file_extension():
    #     return ".lark"
