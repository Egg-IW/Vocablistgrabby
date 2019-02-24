from PyDictionary import PyDictionary
import os
import sys
import csv

sys.stderr = open(os.devnull, 'w')

numcount = int(input("How many terms are in the list you wish to input?"))


while numcount > 0:
    word = input("Please enter a word from the list: ")
    numcount -= 1

    dictionary = PyDictionary()
    ##word = input("Enter a word:")
    print(dictionary.meaning(word))


with open('quizletset.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    #thewriter.writerow([word, dictionary.meaning(word)])
    for lazy in range(0, numcount):
        thewriter.writerow([word, dictionary.meaning(word)])
