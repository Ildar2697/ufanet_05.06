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
    alphabets = {
        'eng': 'abcdefghijklmnopqrstuvwxyz',
        'ru': 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
        'numbers': '0123456789'
    }
    result = ''
    checkInput(text, shift)
    for el in text:
        flag = True
        for alphabet in alphabets.values():
            if el.lower() in alphabet:
                result += shiftLetter(el, alphabet, shift)
                flag = False
                break
        if flag:
            result += el
    return result


def decryptionCaesar(text: str, shift: int) -> str:
    return encryptionCaesar(text, -shift)
