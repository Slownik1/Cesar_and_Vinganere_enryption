from ceasar import *
from vigenere import *

#Cesar encrypt and decrypt
encryptedText = ceasar_encrypt("test1234", 10)
print(encryptedText)
print(ceasar_decrypt(encryptedText, 10))

#Cesar cracker
print(ceasar_cracker(encryptedText))

#Vigrine encrypt and decrypt

encryptedText = vigenere_encrypt("Test1234", "key")
print(encryptedText)
print(vigenere_decrypt(encryptedText, "key"))

