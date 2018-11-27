import string
from words import chooseWord

# End of helper code
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


# Iss function ko test karne ke liye aap getGuessedWord("kindness", [k, n, d]) call kar sakte hai
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: ek string word jo ki user ko guess kar raha hai
    lettersGuessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secretWord = "kindness", lettersGuessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''
    i = 0
    new_word = ""
    while (i < len(secretWord)):
        if secretWord[i] in lettersGuessed:
            new_word += secretWord[i]
        else:
            new_word += "_"
        i += 1
    
    return new_word


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

    Hangman game yeh start karta hai:

    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secretWord mei kitne letters hai

    * Har round mei user se ek letter guess karne ko bolte hai

    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi

    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai

    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    print ""

    lettersGuessed = []
    
    availableLetters = getAvailableLetters(lettersGuessed)
    print "Available letters: " + availableLetters

    guess = raw_input("Please guess a letter: ")
    letter = guess.lower()

    if letter in secretWord:
        lettersGuessed.append(letter)
        print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
        print ""

        if isWordGuessed(secretWord, lettersGuessed) == True:
            print " * * Congratulations, you won! * * "
            print ""

    else:
        print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
        lettersGuessed.append(letter)
        print ""
    
    # if isWordGuessed(secretWord, lettersGuessed) == False:
    #     print "Sorry, you ran out of guesses. The word was " + str(secretWord) + "."

# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secretWord = chooseWord()
hangman(secretWord)