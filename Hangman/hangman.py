# Name: Hossam Asaad
# Time spent:

# Hangman Game
# -----------------------------------

import random
import string

WORDLIST_FILENAME = "words.txt"

# this function to read the words from the file

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')                                   # to read file
    # line: string
    line = inFile.readline()                                                # read line from file
    # wordlist: list of strings
    wordlist = line.split()                                                 # split line to words in list
    print("  ", len(wordlist), "words loaded.")
    return wordlist

# this function is to choose random word for the game

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = load_words()

# this function is to check if player guessed or not

def is_word_guessed(secret_word, letters_guessed):

    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """

    state = True                                                    # set state to store check if word guessed or not
    for letter in secret_word:
        if letter not in letters_guessed:
            state = False
            break
    return state


# this function is to get guessed word by the player


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """

    guessed_word = ""                                                                           # to store guessed word
    for char in secret_word:
        if char in letters_guessed:                                                             # if char is guessed put it
            guessed_word = guessed_word + char
        else:                                                                                   # else put ("_ ")
            guessed_word = guessed_word + "_ "
    return guessed_word                                                                         # return the guessed word

# this function to return the available letters to the player

def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """

    available_letters = list(string.ascii_lowercase)                                            # get all lowercase letters
    for char in letters_guessed:                                                                # remove each char guessed by the player
        available_letters.remove(char)
    return "".join(available_letters)                                                           # return available letters
    
# this function to put the structure of the game and use functions to make the game

def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """

    print("Welcome to the game Hangman!")                                                               # welcome the player
    print("I am thinking of a word that is", len(secret_word), "letters long.")                         # tell the player the length of secret word
    warnings = 3                                                                                        # number of warnings
    print("You have", warnings,"warnings left.")
    print("------------")

    guesses_left = 6                                                                                    # number of guesses
    letter_guessed = []                                                                                 # list to letters guessed by the player

    while guesses_left > 0:

        print("You have", guesses_left, "guesses left.")
        print("Available letters: ", get_available_letters(letter_guessed))
        char = input("Please guess a letter: ")                                                         # get a char from the player
        vowels = ['a', 'e', 'i', 'o', 'u']                                                              # vowels letters cost 2 guesses

        if str.isalpha(char) is True:                                                                   # check if player input a char
            char = str.lower(char)
            if char in letter_guessed:                                                                  # check if player guessed char before
                if warnings > 0:
                    warnings -= 1
                    print("Oops! That is not a valid letter. You have", warnings, "warnings left:",
                          get_available_letters(letter_guessed))
                else:
                    guesses_left -= 1
                    print("Oops! That is not a valid letter. You have", warnings, "warnings left:",
                          get_available_letters(letter_guessed))

            else:
                letter_guessed.append(char)
                if char in secret_word:
                    print("Good guess:", get_guessed_word(secret_word,letter_guessed))
                else:
                    print("Oops That letter is not in my word:", get_guessed_word(secret_word, letter_guessed))
                    if char in vowels:
                        guesses_left -= 2
                    else:
                        guesses_left -= 1

                print("-------------")
                state = is_word_guessed(secret_word,letter_guessed)
                if state is True:
                    print("You guessed thw word you are the winner, the word is",secret_word)
                    print("Your total score for this game is:", guesses_left * len(letter_guessed))
                    break
        else:
            if warnings > 0:
                warnings -= 1
                print("Oops! That is not a valid letter. You have", warnings, "warnings left:", get_guessed_word(secret_word, letter_guessed))
            else:
                guesses_left -= 1
                print("Oops! That is not a valid letter. You have", warnings, "warnings left:", get_guessed_word(secret_word, letter_guessed))

    if guesses_left == 0:
        print("You lose try again, the word is", secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    state = True
    my_word = my_word.replace(" ","")
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if my_word[i] == other_word[i] or my_word[i] == "_":
                continue
            else:
                state = False
                break
    else:
        state = False
    return state



def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    state = False
    for word in wordlist:
        if match_with_gaps(my_word,word) is True:
            if state is False:
                print("Possible word matches are:\n")
                state = True
            print(word,)
    if state is not True:
        print("No matches found")


# this is another version of the game with hints

def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")

    warnings = 3
    print("You have", warnings, "warnings left.")
    print("------------")

    guesses_left = 6
    letter_guessed = []

    while guesses_left > 0:

        print("You have", guesses_left, "guesses left.")
        print("Available letters: ", get_available_letters(letter_guessed))
        char = input("Please guess a letter: ")
        vowels = ['a', 'e', 'i', 'o', 'u']

        if char == "*":
            show_possible_matches(get_guessed_word(secret_word, letter_guessed))
        elif str.isalpha(char) is True:
            char = str.lower(char)
            if char in letter_guessed:
                if warnings > 0:
                    warnings -= 1
                    print("Oops! That is not a valid letter. You have", warnings, "warnings left:",
                          get_available_letters(letter_guessed))
                else:
                    guesses_left -= 1
                    print("Oops! That is not a valid letter. You have", warnings, "warnings left:",
                          get_available_letters(letter_guessed))

            else:
                letter_guessed.append(char)
                if char in secret_word:
                    print("Good guess:", get_guessed_word(secret_word, letter_guessed))
                else:
                    print("Oops That letter is not in my word:", get_guessed_word(secret_word, letter_guessed))
                    if char in vowels:
                        guesses_left -= 2
                    else:
                        guesses_left -= 1

                print("-------------")
                state = is_word_guessed(secret_word, letter_guessed)
                if state is True:
                    print("You guessed thw word you are the winner, the word is", secret_word)
                    print("Your total score for this game is:", guesses_left * len(letter_guessed))
                    break
        else:
            if warnings > 0:
                warnings -= 1
                print("Oops! That is not a valid letter. You have", warnings, "warnings left:",
                      get_guessed_word(secret_word, letter_guessed))
            else:
                guesses_left -= 1
                print("Oops! That is not a valid letter. You have", warnings, "warnings left:",
                      get_guessed_word(secret_word, letter_guessed))
    if guesses_left == 0:
        print("You lose try again, the word is", secret_word)


if __name__ == "__main__":

    # to play version with no hints

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

#######################

    # to play version with hints

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
