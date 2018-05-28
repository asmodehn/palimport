
import filefinder2

from palimport._utils import _verbose_message

from coconut.compiler.compiler import Compiler




class CoconutLoader(filefinder2.machinery.SourceFileLoader):

    def __init__(self, fullname, path):
        """Initializes Coconut's compiler"""
        self.compiler = Compiler()
        super(CoconutLoader, self).__init__(fullname=fullname, path=path)

    # TODO : investigate : removing get_code breaks loader !!!
    def get_code(self, fullname):
        source = self.get_source(fullname)

        _verbose_message('transpiling coconut for "{0}"'.format(fullname))
        pysource = self.compiler.parse_file(source)

        _verbose_message('compiling code for "{0}"'.format(fullname))
        try:
            code = self.source_to_code(pysource, self.get_filename(fullname))
            return code
        except TypeError:
            raise

    def get_source(self, name):
        """Implementing actual python code from file content"""
        path = self.get_filename(name)


        # pypath = CocoCmd.compile_file(path)

        # Returns decoded string from source python file
        pystr = super(CoconutLoader, self).get_source(name)

        return pystr

