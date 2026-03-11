# flake8: noqa
from app.calculator import add, sub
import pytest


class TestCalculator:
    """计算器模块的测试用例"""

    # 使用参数化测试覆盖多种输入情况
    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (10, 20, 30),
        (100, 200, 300),
    ])
    def test_add(self, a, b, expected):
        """测试加法功能"""
        assert add(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (5, 2, 3),
        (0, 0, 0),
        (10, 5, 5),
        (-1, -1, 0),
        (100, 50, 50),
    ])
    def test_sub(self, a, b, expected):
        """测试减法功能"""
        assert sub(a, b) == expected
