import string
import math
import numpy as np
import sys
import string
from sympy import Matrix, pprint

class CaesarCipher:
    def __init__(self, key):
        self.alphabet = string.ascii_lowercase
        self.shiftedAlphabet = self.alphabet[key:] + self.alphabet[:key]

    def encrypt(self, message):
        encryptedMessage = ''
        for character in message:
            if (character.isspace()):
                encryptedMessage += " "
            else:
                index = self.alphabet.index(character)
                encryptedMessage += self.shiftedAlphabet[index]
        return encryptedMessage

    def decrypt(self, message):
        decryptedMessage = ''
        for character in message:
            if (character.isspace()):
                decryptedMessage += " "
            else:
                index = self.shiftedAlphabet.index(character)
                decryptedMessage += self.alphabet[index]
        return decryptedMessage
def getKeyMatrix(key): 
     k = 0
     ke=[0,0,0,0]
     for i in range(4):  
        ke[i]=(ord(key[k]) % 65)
        k += 1
     return ke
def prepare_text(raw_text):
      n=2
      input_text = list(raw_text)
      input_text = list(filter((' ').__ne__, input_text))
      text = np.zeros(len(input_text))
      for a in range(len(input_text)):
          text[a] = ord(input_text[a]) - ord('a')
      print(text)
      l = len(input_text)
      print(l)
      if(l%n !=0 ):
          a = np.ones(n-l%n)*25
          print(a)
          text = np.append(text,a,axis = 0)
      text = text.reshape(int(text.shape[0]/n),n)
      return text
class HillCipher:
    def __init__(self, key):
       self.key=getKeyMatrix(key)
       n = math.sqrt(len(self.key))
       n = int(n)
       self.key = np.array(self.key).reshape(n,n)
       self.key=Matrix(self.key)

    def encryptscytale(self, message):
         n=2
         
         key=self.key
         key = np.array(key).reshape(n,n)
     
         text = prepare_text(message)
         enc = []
         enc_text = ""
         for a in range(len(text)):
             b = np.dot(key,text[a])
             for i in range(len(b)):
                 enc += [b[i]%26]
        
         ind = 0
         for i in range(len(message)):
             if(message[i]!=' '):
                 enc_text += chr(ord('a') + int(enc[ind])) 
                 ind +=1
             else:
                 enc_text += ' '
         return enc_text

    
    
    

    