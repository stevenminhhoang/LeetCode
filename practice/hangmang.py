import random
import string
WORDLIST_FILENAME = "/Users/StevenDao/Developer/LeetCode/practice/words.txt"

def loadWords():
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.splitlines()
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    for char in secretWord:
        if char not in lettersGuessed:
            return False

    return True

def getGuessedWord(secretWord, lettersGuessed):
    count = 0
    guessedWord = ""
    for char in secretWord:
        if char in lettersGuessed:
            count += 1
            guessedWord += char
        else:
            guessedWord += "_"

    return guessedWord

def getAvailableLetters(lettersGuessed):
    res = ""
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            res += letter

    return res

def hangman(secretWord):
    lettersGuessed = set()
    guessesLeft = 8
    while guessesLeft > 0:
        print("Current guessed word: ", getGuessedWord(secretWord, lettersGuessed))
        print('You have' , guessesLeft , 'guesses left.')
        print('Available Letters:' , getAvailableLetters(lettersGuessed))
        guessLetter = input("Please guess a letter: ").lower()

        if guessLetter in secretWord and guessLetter not in lettersGuessed:
            lettersGuessed.add(guessLetter)
            print("Correct letter!")
            # print("Current guessed word: ", getGuessedWord(secretWord, lettersGuessed))
            print("-------------")
            if isWordGuessed(secretWord, lettersGuessed):
                print("You won!")
                break
            guessesLeft -= 1

        elif guessLetter in secretWord and guessLetter in lettersGuessed:
            print("Oops! You've already guessed that letter!")
            # print("Current guessed word: ", getGuessedWord(secretWord, lettersGuessed))
            print("-------------")

        elif guessLetter not in secretWord and guessLetter not in lettersGuessed:
            lettersGuessed.add(guessLetter)
            print("Oops! That letter is not in my word!")
            # print("Current guessed word: ", getGuessedWord(secretWord, lettersGuessed))
            print("-------------")
            guessesLeft -= 1
            if not isWordGuessed(secretWord, lettersGuessed) and guessesLeft == 0:
                print("Sorry, you ran out of guesses! Good luck next time!")
                print("The answer is: ", secretWord)

        elif guessLetter not in secretWord and guessLetter in lettersGuessed:
            print("Oops! You've already guessed that letter!")
            # print("Current guessed word: ", getGuessedWord(secretWord, lettersGuessed))
            print("-------------")



wordlist = loadWords()
secretWord = chooseWord(wordlist)
hangman("helloworld")
