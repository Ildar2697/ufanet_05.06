import main
import pytest


def test_encryptionCaesarRaizesValueErrorOnIncorrectArgumentTypes():
    with pytest.raises(ValueError):
        main.encryptionCaesar('Text', '1')
        main.encryptionCaesar(123455, 1)


@pytest.mark.parametrize("text,shift", [('ABCxyz', 8), ("АБВ", 1), ('123', 2), ('', 1), ('!@$@%@##', 1), ('aBcDeFgЭюЯ21', 20), ('üüüуацу1231 ФФVVV', 4), ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 5)])
def test_encryptionCaesardecryptionCaesarRetunsInitialValue(text, shift):
    encrypted_text = main.encryptionCaesar(text, shift)
    assert main.decryptionCaesar(encrypted_text, shift) == text


@pytest.mark.parametrize('text,shift,expected', [('ABC', 1, 'BCD'), ('АБВ', 1, 'БВГ'), ('XyZ', 2, 'ZaB'), ('123Привет321Hello', -1, '012Опзбдс210Gdkkn')])
def test_encryptionCaesarReturnsExpected(text, shift, expected):
    assert main.encryptionCaesar(text, shift) == expected


@pytest.mark.parametrize('text,shift,expected', [('BCD', 1, 'ABC'), ('БВГ', 1, 'АБВ'), ('ZaB', 2, 'XyZ'), ('012Опзбдс210Gdkkn', -1, '123Привет321Hello')])
def test_decryptionCaesarRetunsExpected(text, shift, expected):
    assert main.decryptionCaesar(text, shift) == expected


