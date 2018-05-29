import palimport

with palimport.CoconutImporter():
    if __package__:  # attempting relative import when possible
        from . import fact
    else:
        import fact

import pytest

#import coconut
#import coconut.convenience  # should be enough to setup the importer in metapath (actually turning on autocompilation)


def test_fact_neg():
    with pytest.raises(fact.MatchError):
        fact.factorial(-1)


def test_fact_nint():
    with pytest.raises(fact.MatchError):
        fact.factorial(0.5)


def test_fact_stop():
    assert fact.factorial(0) == 1


def test_fact():
    assert fact.factorial(3) == 6
