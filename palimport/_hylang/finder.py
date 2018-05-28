from __future__ import absolute_import, division, print_function

"""
A module to setup custom importer for .hy files

"""

# We need to be extra careful with python versions
# Ref : https://docs.python.org/dev/library/importlib.html#importlib.import_module

import os

from filefinder2.machinery import FileFinder as filefinder2_FileFinder

from .._utils import _ImportError


class HyFinder(filefinder2_FileFinder):
    """PathEntryFinder to handle finding Lark grammars"""

    def __init__(self, path, *loader_details):
        super(HyFinder, self).__init__(path, *loader_details)

    def __repr__(self):
        return 'HyFinder({!r})'.format(self.path)

    @classmethod
    def path_hook(cls, *loader_details):
        """A class method which returns a closure to use on sys.path_hook
        which will return an instance using the specified loaders and the path
        called on the closure.

        If the path called on the closure is not a directory, or doesnt contain
         any files with the supported extension, ImportError is raised.

         This is different from default python behavior
         but prevent polluting the cache with custom finders
        """
        def path_hook_for_HyFinder(path):
            """Path hook for importlib.machinery.FileFinder."""

            if not (os.path.isdir(path)):
                raise _ImportError('only directories are supported')

            exts = [x for ld in loader_details for x in ld[1]]
            if not any(fname.endswith(ext) for fname in os.listdir(path) for ext in exts):
                raise _ImportError(
                    'only directories containing {ext} files are supported'.format(ext=", ".join(exts)),
                    path=path)
            return cls(path, *loader_details)

        return path_hook_for_HyFinder

    def find_spec(self, fullname, target=None):
        """
        Try to find a spec for the specified module.
        :param fullname: the name of the package we are trying to import
        :return: the matching spec, or None if not found.
        """

        # We attempt to load a .hy file as a module
        tail_module = fullname.rpartition('.')[2]
        base_path = os.path.join(self.path, tail_module)
        for suffix, loader_class in self._loaders:
            full_path = base_path + suffix
            if os.path.isfile(full_path):  # maybe we need more checks here (importlib filefinder checks its cache...)
                return self._get_spec(loader_class, fullname, full_path, None, target)

        # Otherwise, we try find python modules (to be able to embed .lark files within python packages)
        return super(HyFinder, self).find_spec(fullname=fullname, target=target)


