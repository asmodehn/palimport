from __future__ import absolute_import

import contextlib
import functools
import os
import sys

# we rely on filefinder2 as a py2/3 wrapper of importlib
import filefinder2
import six
from ._utils import _verbose_message

import filefinder2.machinery


# Importing Parser's Grammar importers
from ._lark import Importer as LarkImporter


from ._hylang import Importer as HyImporter


from .finder import Finder
from .loader import Loader


def Importer(loader, extensions):

    class CustomImporter(filefinder2.Py3Importer):
        def __enter__(self):
            super(CustomImporter, self).__enter__()

            # we hook the grammar customized loader
            self.path_hook = Finder.path_hook((loader, extensions), )

            if self.path_hook not in sys.path_hooks:
                ffidx = sys.path_hooks.index(filefinder2.ff_path_hook)
                sys.path_hooks.insert(ffidx, self.path_hook)

        def __exit__(self, exc_type, exc_val, exc_tb):
            # removing path_hook
            sys.path_hooks.pop(sys.path_hooks.index(self.path_hook))

            super(CustomImporter, self).__exit__(exc_type, exc_val, exc_tb)

    # Instantiating CustomImporter right away to enter context
    return CustomImporter()


__all__ = [
    'LarkImporter',
    'Importer',
]



