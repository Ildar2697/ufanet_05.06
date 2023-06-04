import main
import pytest


def test_encryptionCaesarRaizesValueErrorOnIncorrectArgumentTypes():
    with pytest.raises(ValueError):
        main.encryptionCaesar('Text', '1')
        main.encryptionCaesar(123455, 1)


@pytest.mark.parametrize("text,shift", [('ABCxyz', 8), ("АБВ", 1), ("123", 2), ('', 1), ('!@$@%@##', 1)])
def test_encryptionCaesardecryptionCaesarRetunsInitialValue(text, shift):
    encrypted_text = main.encryptionCaesar(text, shift)
    print(text, shift, encrypted_text)
    assert main.decryptionCaesar(encrypted_text, shift) == text
