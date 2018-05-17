import pytest
from lark import Lark

import palimport.lark

from ..interp import interp, CalcLoader

# Testing Parsing with inline transformation
# In our case here, it does computation


def test_calc_add():

    assert interp("3 + 2", ) == "5.0"


def test_calc_sub():

    assert interp("3 - 2", ) == "1.0"


def test_calc_mul():

    assert interp("3 * 2", ) == "6.0"


def test_calc_div():

    assert interp("3 / 2", ) == "1.5"


def test_calc_assign():

    assert interp("b = 2", ) == "b = 2.0"


def test_module_import():
    with palimport.lark.importer(CalcLoader, ['.calc']):
        from .. import theanswer

    assert theanswer.ANSWER == 42




if __name__ == '__main__':
    pytest.main(['-s'])
