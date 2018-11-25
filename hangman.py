import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Ye function kafi jayada words ko load karne mai help karega
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    ye function ek word randomly return karega
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: ek string word jo ki user ko guess karna hai
    lettersGuessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secretWord mai hai, warna no
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    # remove this return
    return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: ek string word jo ki user ko guess kar raha hai
    lettersGuessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secretWord = "kindness", lettersGuessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''
    # FILL IN YOUR CODE HERE...

    # FILL IN YOUR CODE HERE...
    # remove this return
    return '________'


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar lettersGuessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
    # FILL IN YOUR CODE HERE...

    import string
    lettersLeft = string.ascii_lowercase

    # FILL IN YOUR CODE HERE...
    # remove this return
    return lettersLeft

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    print "-----------"

    lettersGuessed = []
    availableLetters = getAvailableLetters(lettersGuessed)
    guessesLeft = 8
    while guessesLeft > 0:
        print "You have " + str(guessesLeft) + " guesses left."
        print "Available letters: " + availableLetters
        guess = raw_input("Please guess a letter: ")
        letter = guess.lower()
        if letter in lettersGuessed:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            print "-----------"
        elif letter in secretWord:
            lettersGuessed.append(letter)
            print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
            availableLetters = getAvailableLetters(lettersGuessed)
            print "-----------"
            if isWordGuessed(secretWord, lettersGuessed) == True:
             print "Congratulations, you won!"
             break
        else:
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
            guessesLeft = guessesLeft - 1
            lettersGuessed.append(letter)
            availableLetters = getAvailableLetters(lettersGuessed)
            print "-----------"
    if isWordGuessed(secretWord, lettersGuessed) == False:
        print "Sorry, you ran out of guesses. The word was " + str(secretWord) + "."




# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)