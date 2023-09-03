import pytest
from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_srt():
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"


def test_change_lang():
    kb.change_lang()
    assert str(kb.language) == "RU"


def test_double_change_lang():
    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"


#def test_error():
#    with pytest.raises(AttributeError):
#        kb.language = 'CH'
