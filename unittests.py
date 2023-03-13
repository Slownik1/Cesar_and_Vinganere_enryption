import unittest
from ceasar import *
from vigenere import *

class TestApp():

    text = "aaa"
    key = 1
    encryptedText = "bbb"

    def testCesarEncryptt(self, text, key, encryptedText):
        self.assertEqual(ceasar_encrypt(text, key), encryptedText)

    def testCesarDecrypt(self, text, key, encryptedText):
        self.assertEqual(ceasar_decrypt(encryptedText, key), text)

    def testViganereEncrypt(self, text, key, encrptedText):
        self.assertEqual(vigenere_encrypt(text, key), encrptedText)

    def testViganereDecrypt(self, text, key,encryptedText):
        self.assertEquals(vigenere_decrypt(encryptedText, key), text)



unittest.main()

