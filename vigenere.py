import string

def vigenere_encrypt(text, key):
    alphabet = string.ascii_lowercase
    key = key.lower()
    key_len = len(key)
    ciphertext = ""
    for i, char in enumerate(text):
        if char in alphabet:
            key_idx = i % key_len
            shift = alphabet.index(key[key_idx])
            idx = (alphabet.index(char) + shift) % 26
            ciphertext += alphabet[idx]
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(encryptedText, key):
    alphabet = string.ascii_lowercase
    key = key.lower()
    key_len = len(key)
    text = ""
    for i, char in enumerate(encryptedText):
        if char in alphabet:
            key_idx = i % key_len
            shift = alphabet.index(key[key_idx])
            idx = (alphabet.index(char) - shift) % 26
            text += alphabet[idx]
        else:
            text += char
    return text