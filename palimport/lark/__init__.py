from __future__ import absolute_import

import contextlib
import functools
import os
import sys

# we rely on filefinder2 as a py2/3 wrapper of importlib
import filefinder2

from ._utils import _verbose_message

from ._lark_finder import LarkFinder
from ._lark_loader import LarkLoader


@contextlib.contextmanager
def importer(*args, **kwargs):
    """Install the path-based import components."""
    # We should plug filefinder first to avoid plugging ROSDirectoryFinder, when it is not a ROS thing...

    with filefinder2.enable_pep420():  # TODO : dont force it on py3 if not debugging

        # Resetting sys.path_importer_cache to get rid of previous importers
        sys.path_importer_cache.clear()

        _lfh = LarkFinder.path_hook((functools.partial(LarkLoader, *args, **kwargs), ['.lark']))

        if _lfh not in sys.path_hooks:
            # todo : better before or after ?
            sys.path_hooks.insert(filefinder2.get_filefinder_index_in_path_hooks(), _lfh)

        # if LarkPathFinder not in sys.meta_path:
        #     #  todo : really necessary ?
        #     sys.meta_path.insert(filefinder2.get_pathfinder_index_in_meta_hooks(), LarkPathFinder)

        yield

        # CAREFUL : Even though we remove the path from sys.path,
        # initialized finders will remain in sys.path_importer_cache

        # #  removing meta_path
        # sys.meta_path.pop(sys.meta_path.insert(LarkPathFinder))

        # removing path_hook
        sys.path_hooks.pop(sys.path_hooks.index(_lfh))

    # Resetting sys.path_importer_cache to get rid of previous importers
    sys.path_importer_cache.clear()


__all__ = [
    'importer',
]