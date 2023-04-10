import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_phone_init(phone):
    """
    Тест конструктора класса Phone
    """
    assert isinstance(phone, Phone)
    assert phone.name == 'iPhone 14'
    assert phone.price == 120_000
    assert phone.quantity == 5


def test_number_of_sim(phone):
    assert phone.number_of_sim == 2
    if phone.number_of_sim <= 0:
        assert ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')


def test___repr__(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"
    assert isinstance(repr(phone), str)


