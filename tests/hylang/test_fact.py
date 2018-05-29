import palimport


with palimport.HyImporter():
    if __package__:  # attempting relative import when possible
        from . import fact
    else:
        import fact


def test_fact():
    assert fact.factorial(5) == 120
