import pytest

from pythoncode.calculator import Calculator


# @pytest.mark.parametrize('a,b,expect', [
#     (3, 5, 8), (-1, -2, -3), (100, 300, 500)
# ], ids=['int', 'minus', 'bigint'])
class TestCalc:

    def setup_class(self):
        self.calc = Calculator()
        print('Start calculation...')

    def teardown_class(self):
        print('End calculation')

    @pytest.mark.parametrize('a,b,expect', [
        (3, 5, 8), (-1, -2, -3), (100, 300, 500)
    ], ids=['int', 'minus', 'bigint'])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize('a,b,expect', [
        (3, 5, -2), (-1, -2, 1), (300, 300, 10)
    ], ids=['int', 'minus', 'bigint'])
    def test_minus(self, a, b, expect):
        assert expect == self.calc.minus(a, b)

    @pytest.mark.parametrize('a,b,expect', [
        (3, 5, 12), (-1, -2, 2), (300, 4, 1200)
    ], ids=['int', 'minus', 'bigint'])
    def test_mul(self, a, b, expect):
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize('a,b,expect', [
        (3, 5, 0.6), (-4, -2, 2), (400, 100, 3)
    ], ids=['int', 'minus', 'bigint'])
    def test_div(self, a, b, expect):
        assert expect == self.calc.div(a, b)