from PyDictionary import PyDictionary
import os
import sys
import csv

sys.stderr = open(os.devnull, 'w')

numcount = int(input("How many terms are in the list you wish to input?"))

dictionary = PyDictionary()
definitions = []
for _ in range(numcount):
    word = input("Please enter a word from the list: ")
    meaning = dictionary.meaning(word)
    defin_pair = (word, meaning)
    definitions.append(defin_pair)
    print(defin_pair)


with open('quizletset.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    for defin in definitions:
        thewriter.writerow(defin)
