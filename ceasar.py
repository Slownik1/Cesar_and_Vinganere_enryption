import string

def ceasar_encrypt(text, shift):
    alphabet = string.printable
    encryptedText = ""
    for char in text:
        if char in alphabet:
            idx = (alphabet.index(char) + shift)
            encryptedText += alphabet[idx]
        else:
            encryptedText += char
    return encryptedText

def ceasar_decrypt(text, shift):
    alphabet = string.printable
    encryptedText = ""
    for char in text:
        if char in alphabet:
            idx = (alphabet.index(char) - shift)
            encryptedText += alphabet[idx]
        else:
            encryptedText += char
    return encryptedText

def ceasar_cracker(text):
    alphabet = string.printable
    for shift in range(1, 100):
        crackedText = ""
        for char in text:
            if char in alphabet:
                idx = (alphabet.index(char) - shift)
                crackedText += alphabet[idx]
            else:
                crackedText += char
        print(f"Shift={shift}: {crackedText}")