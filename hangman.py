import string
import random
from words import choose_word
from images import IMAGES
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

def hint(secret_word,letters_guessed):
    r_hint=''
    while True:
        r_hint=random.choice(secret_word)
        if r_hint in letters_guessed:
            continue
        else:
            return r_hint

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''

    for x in secret_word:
        if x not in letters_guessed:
            return False

    return True

# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word

def isValid(letter):
    length=len(letter)
    if (length==1) & (letter >='a') & (letter <='z') :
        print(letter)
        return True
    return False

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    letters_left = string.ascii_lowercase
    for x in letters_guessed:
        letters_left=letters_left.replace(x,'')
    return letters_left


def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    # print(secret_word)

    letters_guessed = []
    count=8
    h=0
    while count!=0 :
        available_letters = get_available_letters(letters_guessed)
        print("\nAvailable letters: {} ".format(available_letters))
        print("\nIf hint is needed thn type hint")
        guess = input("Please guess a letter: ")
        letter = guess.lower()

        if (letter=="hint") :
            
            if not h:
                print(hint(secret_word,letters_guessed))
                h=1
            else:
                print("\nHint is provided only once")
            continue

        if isValid(letter)==False:
            print("\nPlease enter a character from")
            continue

        if letter in letters_guessed:
            print("\nLetter already guessed. Try another letter")
            continue

        if letter in secret_word:

            letters_guessed.append(letter)
            print("Good guess: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
                break
        else:
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            letters_guessed.append(letter)
            count-=1
            print("\n only {} remaining lives".format(count))
            print(IMAGES[count]+"\n\n")
    if count==0:
        print("\nSorry, You lost the game :( \n The correct word is " + secret_word)

# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
