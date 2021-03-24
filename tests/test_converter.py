import pytest
from mojiconverter.app import katakana


def test_katakana():
    """ Test that checks the conversion of hiragana to katakana"""
    input_str = "こんにちは"
    assert katakana(input_str) == "こんにちは"