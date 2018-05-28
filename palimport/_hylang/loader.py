import __future__

import os
import filefinder2

from palimport._utils import _verbose_message, _ImportError

from hy.compiler import hy_compile, HyTypeError
from hy.models import HyObject, HyExpression, HySymbol, replace_hy_obj
from hy.lex import tokenize, LexException

import marshal

from hy._compat import PY3, PY37, MAGIC, builtins, long_type, wr_long
from hy._compat import string_types


class HyLoader(filefinder2.machinery.SourceFileLoader):

    def set_data(self, path, data):
        """Optional method which writes data (bytes) to a file path (a str).
        Implementing this method allows for the writing of bytecode files.
        """
        st = os.stat(path)
        timestamp = long_type(st.st_mtime)

        cfile = filefinder2.util.cache_from_source(path)
        try:
            os.makedirs(os.path.dirname(cfile))
        except (IOError, OSError):
            pass

        with builtins.open(cfile, 'wb') as fc:
            fc.write(MAGIC)
            if PY37:
                # With PEP 552, the header structure has a new flags field
                # that we need to fill in. All zeros preserve the legacy
                # behaviour, but should we implement reproducible builds,
                # this is where we'd add the information.
                wr_long(fc, 0)
            wr_long(fc, timestamp)
            if PY3:
                wr_long(fc, st.st_size)
            marshal.dump(data, fc)
                
    # TODO : investigate : removing get_code breaks loader !!!
    def get_code(self, fullname):
        source = self.get_source(fullname)
        _verbose_message('compiling code for "{0}"'.format(fullname))
        try:
            code = self.source_to_code(source, self.get_filename(fullname), fullname)
            return code
        except TypeError:
            raise

    def source_to_code(self, data, path, module_name=None):
        """Compile source to HST, then to AST.
        module_name parameter has been added compared to python API, to be able to pass it to hy_compile"""
        hst = HyExpression([HySymbol("do")] + tokenize(data + "\n"))
        ast = hy_compile(hst, module_name)
        flags = (__future__.CO_FUTURE_DIVISION | __future__.CO_FUTURE_PRINT_FUNCTION)
        return compile(ast, path, "exec", flags)
