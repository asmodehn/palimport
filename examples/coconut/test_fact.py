
import coconut
import coconut.convenience  # should be enough to setup the importer in metapath (actually turning on autocompilation)

from . import fact


def test_fact():
    assert fact.factorial(5) == 120
