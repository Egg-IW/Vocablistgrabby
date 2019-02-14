from PyDictionary import PyDictionary
import os
import sys
sys.stderr = open(os.devnull, 'w')

dictionary = PyDictionary()
word = input("Enter a word:")
print(dictionary.meaning(word))
