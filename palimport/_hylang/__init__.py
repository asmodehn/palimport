from __future__ import absolute_import

import sys
import filefinder2

# we rely on filefinder2 as a py2/3 wrapper of importlib

from .finder import HyFinder
from .loader import HyLoader


class Importer(filefinder2.Py3Importer):

    def __enter__(self):
        super(Importer, self).__enter__()

        # we hook the grammar customized loader
        self.path_hook = HyFinder.path_hook((HyLoader, ['.hy']), )

        if self.path_hook not in sys.path_hooks:
            ffidx = sys.path_hooks.index(filefinder2.ff_path_hook)
            sys.path_hooks.insert(ffidx, self.path_hook )

    def __exit__(self, exc_type, exc_val, exc_tb):

        # removing path_hook
        sys.path_hooks.pop(sys.path_hooks.index(self.path_hook))

        super(Importer, self).__exit__(exc_type, exc_val, exc_tb)


__all__ = [
    Importer
]
