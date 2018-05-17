import pytest
import palimport.lark

"""
Module testing that the calc.lark grammar actually parses string as expected
"""

with palimport.lark.importer(palimport.lark.LarkGrammarLoader, ['.lark']) as lark_parser:
    from .. import calc

def test_calc_add():

    assert calc.parser.parse("3 + 2", ).pretty() == """add
  number\t3
  number\t2
"""


def test_calc_sub():

    assert calc.parser.parse("3 - 2", ).pretty() == """sub
  number\t3
  number\t2
"""


def test_calc_mul():

    assert calc.parser.parse("3 * 2", ).pretty() == """mul
  number\t3
  number\t2
"""


def test_calc_div():

    assert calc.parser.parse("3 / 2", ).pretty() == """div
  number\t3
  number\t2
"""


def test_calc_assign():

    assert calc.parser.parse("b = 2", ).pretty() == """assign_var
  b
  number\t2
"""


if __name__ == '__main__':
    pytest.main(['-s'])
