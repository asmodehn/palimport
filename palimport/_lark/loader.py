
import filefinder2

from palimport._utils import _verbose_message

# to debug import problems before attempting to import dynamically
from lark import Lark


class LarkLoader(filefinder2.machinery.SourceFileLoader):

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
        larkstr = super(LarkLoader, self).get_source(name)
        larkstr = "from lark import Lark; parser = Lark(\"\"\"{larkstr}\"\"\", parser='lalr')""".format(**locals())

        return larkstr

