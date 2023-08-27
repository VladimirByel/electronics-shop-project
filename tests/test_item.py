"""
Здесь надо написать тесты с использованием pytest для модуля item.
"""

from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


Item.pay_rate = 0.8


def test_apply_discount():
    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name():
    assert item1.name == 'Смартфон'
    assert item2.name == 'Ноутбук'


def test_setter_name():
    item1.name = 'Телефон'
    item2.name = 'Компьютер'
    assert item1.name == 'Телефон'
    assert item2.name == 'Компьютер'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_str_and_repr():
    assert repr(item1) == "Item('Телефон', 8000.0, 20)"
    assert str(item1) == 'Телефон'
