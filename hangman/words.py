import string
import random
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded.\n"
    return wordlist

def chooseWord():
    """
    wordlist (list): list of words (strings)
    ye function ek word randomly return karega
    """
    wordlist = loadWords()
    secretWord = random.choice(wordlist)
    secretWord = secretWord.lower()

    return secretWord