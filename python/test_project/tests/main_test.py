import sys

sys.path.append("../")
from main import judge_even_or_odd


class TestEvenOrOdd:
    def test_even(self):
        assert judge_even_or_odd(2) == "even"

    def test_odd(self):
        assert judge_even_or_odd(3) == "odd"
