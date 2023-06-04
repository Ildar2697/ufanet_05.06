def shiftLetterLowercase(el: str, alphabet: str, shift: int) -> str:
    alphabet_len = len(alphabet)
    i = alphabet.index(el.lower()) + shift
    el_i = i % alphabet_len
    return alphabet[el_i]


def shiftLetter(el: str, alphabet: str, shift: int) -> str:
    letter = shiftLetterLowercase(el, alphabet, shift)
    if el.isupper():
        return letter.upper()
    return letter


def checkInput(text, shift):
    if type(text) != str:
        raise ValueError('Text must be str')
    if type(shift) != int:
        raise ValueError('Shift must be int')


def encryptionCaesar(text: str, shift: int) -> str:
    ru_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    eng_alphabet = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    result = ''
    checkInput(text, shift)
    for el in text:
        if el.lower() in ru_alphabet:
            result += shiftLetter(el, ru_alphabet, shift)
        elif el.lower() in eng_alphabet:
            # result += '3'
            result += shiftLetter(el, eng_alphabet, shift)
        elif el.lower() in numbers:
            result += shiftLetter(el, numbers, shift)
        else:
            result += el
    return result


def decryptionCaesar(text: str, shift: int) -> str:
    return encryptionCaesar(text, -shift)



