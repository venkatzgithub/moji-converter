import pytest
from mojiconverter.app import katakana,hiragana


def test_katakana():
    """ Test that checks the conversion of hiragana to katakana"""
    input_str = "こんにちは"
    assert katakana(input_str) == "コンニチハ"

def test_hiragana():
    """ Test that checks the conversion of katakana to hiragana"""
    input_str = "コンニチハ"
    assert hiragana(input_str) == "こんにちは"