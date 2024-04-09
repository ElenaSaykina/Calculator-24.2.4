import pytest

from app.calc import Calculator()

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_multiply(self):
        assert self.calc.multiply(3, 4) == 12

    def test_division(self):
        assert self.calc.division(10, 2) == 5

    def test_subtraction(self):
        assert self.calc.subtraction(10, 5) == 5

    def test_adding(self):
        assert self.calc.adding(3, 7) == 10

    def teardown(self):
        print("Тест завершён")