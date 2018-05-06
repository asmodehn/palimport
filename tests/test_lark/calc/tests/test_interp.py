import pytest
from lark import Lark

from ..interp import calc

# Testing Parsing with inline transformation
# In our case here, it does computation


def test_calc_add():

    assert calc("3 + 2", ) == 5.0


def test_calc_sub():

    assert calc("3 - 2", ) == 1.0


def test_calc_mul():

    assert calc("3 * 2", ) == 6.0


def test_calc_div():

    assert calc("3 / 2", ) == 1.5


def test_calc_assign():

    assert calc("b = 2", ) == 2








if __name__ == '__main__':
    pytest.main(['-s'])
