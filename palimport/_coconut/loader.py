
import filefinder2

from palimport._utils import _verbose_message

from coconut.command import Command


CocoCmd = Command()


class CoconutLoader(filefinder2.machinery.SourceFileLoader):

    # TODO : investigate : removing get_code breaks loader !!!
    def get_code(self, fullname):
        source = self.get_source(fullname)
        _verbose_message('compiling code for "{0}"'.format(fullname))
        try:
            code = self.source_to_code(source, self.get_filename(fullname))
            return code
        except TypeError:
            raise

    def get_source(self, name):
        """Implementing actual python code from file content"""
        path = self.get_filename(name)

        _verbose_message('transpiling coconut for "{0}"'.format(path))
        pypath = CocoCmd.compile_file(path)

        # Returns decoded string from source python file
        pystr = super(CoconutLoader, self).get_source(name)

        return pystr

