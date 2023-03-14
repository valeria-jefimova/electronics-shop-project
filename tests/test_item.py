"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item1):
    assert item1.calculate_total_price()==200000

