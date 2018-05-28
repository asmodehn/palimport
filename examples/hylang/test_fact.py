
import hy

from . import fact


def test_fact():
    assert fact.factorial(5) == 120
