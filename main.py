def getInput():
    k = int(input("Enter k: "))
    text = input("Enter a text to encrypt: ")
    return (k, text)


def changeEl(el: str, alphabet: str, k: int) -> str:
    alphabet_len = len(alphabet)
    i = alphabet.index(el.lower()) + k
    el_i = i % alphabet_len
    return alphabet[el_i]


def isUpper(el: str, alphabet: str, k: int) -> str:
    letter = changeEl(el, alphabet, k)
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
            result += isUpper(el, ru_alphabet, shift)
        elif el.lower() in eng_alphabet:
            result += isUpper(el, eng_alphabet, shift)
        elif el.lower() in numbers:
            result += isUpper(el, numbers, shift)
        else:
            result += el
    return result

print(encryptionCaesar('ABcd_WXyz__АБвг_ЬЭюя', 1))
print(encryptionCaesar("12334", "1"))


def displayResult(result):
    print(result)
