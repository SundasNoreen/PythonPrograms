# Programming Fundamentals (Lab)
# Problem Set 3 - HangMan
# Submitted By: Sundas Noreen

import random                    # Function to generate Random strings.
import string                    # String Function.

WORDLIST_FILENAME = "words.txt"

def load_words():       # This Function will read the Files and load all the words.
    print("Wait, We are loading words ....")
    inFile = open(WORDLIST_FILENAME, "r")    
    contents= inFile.readline()
    wordlist = contents.split()
    print("  ", len(wordlist), "Words Loaded.")
    return wordlist

wordlist = load_words()         # Now the List of Words can be accessed from anywhere in the Program

def choose_word(wordlist):        # This Function will generate a random Word from the List.
    word_generated=random.choice(wordlist)
    return word_generated

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word:string,the word the user is guessing; assumes all letters are lowercase.
    letters_guessed: list (of letters), which letters have been guessed so far; assumes 
                     that all letters are lowercase.
    returns: boolean, True if all the letters of secret_word are in letters_guessed; False otherwise
    '''
    for char in secret_word:
        if (char in letters_guessed) == False:
            guessed = False
            break
        else:
            guessed = True
    return guessed

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing.
    letters_guessed: list (of letters), which letters have been guessed so far.
    returns: string, comprised of letters, underscores (_), and spaces that represents
             which letters in secret_word have been guessed so far.
    '''
    correct = []            # Keeping track of correct letters.
    guessed_string = "" 
    for i in letters_guessed:
      if i in secret_word:
        correct.append(i)  # If the guessed letter is in secret_word, then store that letter in the correct list.
    
    for char in secret_word:
      if char in correct:
        guessed_string += char
      else:
        guessed_string += "_  "
    return guessed_string        # A string comprising of guessed letters and underscores.


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far.
    returns: string (of letters), comprised of letters that represents which letters have not
             yet been guessed.
    '''
    letters = string.ascii_lowercase      # Get all available letters in lowercase.
    unguessed = " "
    for char in letters:
      if char not in letters_guessed:
        unguessed += char
    return unguessed                      # Return all the letters that are not guessed yet. 

def hangman (secret_word):
    print("Welcome to the game Hangman !!")
    print("I am thinking of a word that is " + str(len(secret_word)) +" letters long.")
    print("_________________________________________________")
    print("You have 3 Warnings Left.")
    letters_guessed = []
    warnings=3
    guesses = 6
    # Loop will continue till Number of Guesses End or User guesses the Word.
    while not is_word_guessed(secret_word, letters_guessed) and guesses > 0:
        print(letters_guessed)
        print("You have " + str(guesses) +" guesses left.")
        print("Available Letters: " + get_available_letters(letters_guessed))
        
        while True:
            guessLetter = input("Please guess a Letter: ").lower()
            if not guessLetter.isalpha():  # If user doesn't enter a valid Letter.
                 if warnings>0:
                     warnings-=1
                     print("Oops! This is not a valid Letter.You have ",warnings,"warnings left.")
                     print(get_guessed_word(secret_word, letters_guessed))
                     print("_________________________________________________")
                     print("Available Letters: " , get_available_letters(letters_guessed))
                     
                 elif warnings==0 and guesses>0:
                     print("Oops! This is not a valid Letter. You have no guesses left, So you loose 1 guess.")
                     print(get_guessed_word(secret_word, letters_guessed))
                     print("_________________________________________________")
                     print("    You have " + str(guesses) +" guesses left")
                     print("Available Letters: " , get_available_letters(letters_guessed))
                
            else:
                if guessLetter in letters_guessed: # If user Repeats a letter.
                    if warnings>0:
                        warnings-=1
                        print("Oops! You've already guessed that letter, You have ",warnings,"warnings left.")
                        print("Available Letters: " , get_available_letters(letters_guessed))
                    elif warnings==0 and guesses>0:
                        print("Oops! You've already guessed that letter: " , get_guessed_word(secret_word, letters_guessed))
                        print("_________________________________________________")
                        print("    You have " + str(guesses) +" guesses left")
                        print("Available Letters: " , get_available_letters(letters_guessed))
                
                else:
                    break
        letters_guessed += guessLetter
        
        if is_word_guessed(secret_word, letters_guessed):  # If user guesses all letters correctly.
            print("Good guess: " , get_guessed_word(secret_word, letters_guessed))
            print("_________________________________________________")
            print("Congratulations, you won!")
            break
    
        elif guessLetter in secret_word:    # If a certain character is guessed true.
             print("Good guess !! " , get_guessed_word(secret_word, letters_guessed))
             print("_________________________________________________")
        
        else:
            if guessLetter in  ['a', 'e', 'i', 'o', 'u']:
                guesses-=2
                print("Oops! That letter is not in my word: " , get_guessed_word(secret_word, letters_guessed))
                print("_________________________________________________")
            else:
                guesses -= 1
                print("Oops! That letter is not in my word: " , get_guessed_word(secret_word, letters_guessed))
                print("____________________________________")
        
        if guesses == 0:
            print("Sorry, you ran out of guesses. The word was " + secret_word + ".")


# Function to match the current guessed word.
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word.
    other_word: string, regular English word.
    returns: boolean, True if all the actual letters of my_word match the 
             corresponding letters of other_word, or the letter is the special symbol
             _ , and my_word and other_word are of the same length;
             False otherwise: 
    '''
    num = 0
    my_word = my_word.replace(' ', '')
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if my_word[i] == '_' or my_word[i] == other_word[i]:
                pass
            else:
                num += 1
        if num == 0:
            return True
        else:
            return False
    else:
        return False

# Function to show all Possible Matches.
def show_possible_matches(my_word):
    list = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            list.append(word)
    if len(list) != 0:
        print(' '.join(list))
    else:
        print('No matches found')
        
def hangman_with_hints (secret_word):
    '''
    my_word: string with _ characters, current guess of secret word.
    returns: nothing, but should print out every word in wordlist that matches my_word.
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    print("Welcome to the game Hangman !!")
    print("I am thinking of a word that is " + str(len(secret_word)) +" letters long.")
    print("_________________________________________________")
    print("You have 3 Warnings Left.")
    letters_guessed = []
    warnings=3
    guesses = 6
    # Loop will continue till Number of Guesses End or User guesses the Word.
    while not is_word_guessed(secret_word, letters_guessed) and guesses > 0:
        print(letters_guessed)
        print("You have " + str(guesses) +" guesses left.")
        print("Available Letters: " + get_available_letters(letters_guessed))
        
        while True:
            guessLetter = input("Please guess a Letter: ").lower()
            if not guessLetter.isalpha():  # If user doesn't enter a valid Letter.
                 if guessLetter=='*':      # Show all Possible Matches, if user types asterisk.
                     show_possible_matches(get_guessed_word(secret_word, letters_guessed))
                 elif warnings>0:
                     warnings-=1
                     print("Oops! This is not a valid Letter.You have ",warnings,"warnings left.")
                     print(get_guessed_word(secret_word, letters_guessed))
                     print("_________________________________________________")
                     print("Available Letters: " , get_available_letters(letters_guessed))
                     
                 elif warnings==0 and guesses>0:
                     print("Oops! This is not a valid Letter. You have no guesses left, So you loose 1 guess.")
                     print(get_guessed_word(secret_word, letters_guessed))
                     print("_________________________________________________")
                     print("    You have " + str(guesses) +" guesses left")
                     print("Available Letters: " , get_available_letters(letters_guessed))
                
            else:
                if guessLetter in letters_guessed:   # If user repeats a letter.
                    if warnings>0:
                        warnings-=1
                        print("Oops! You've already guessed that letter, You have ",warnings,"warnings left.")
                        print("_________________________________________________")
                        print("Available Letters: " , get_available_letters(letters_guessed))
                    elif warnings==0 and guesses>0:
                        print("Oops! You've already guessed that letter: " , get_guessed_word(secret_word, letters_guessed))
                        print("_________________________________________________")
                        print("    You have " + str(guesses) +" guesses left")
                        print("Available Letters: " , get_available_letters(letters_guessed))
                
                else:
                    break
        letters_guessed += guessLetter
        
        if is_word_guessed(secret_word, letters_guessed): # If user guesses all letters correctly.
            print("Good guess: " , get_guessed_word(secret_word, letters_guessed))
            print("_________________________________________________")
            print("Congratulations !! You won.")
            break
    
        elif guessLetter in secret_word:        # If a certain character is guessed true.
             print("Good guess !! " , get_guessed_word(secret_word, letters_guessed))
             print("_________________________________________________")
        
        else:
            if guessLetter in  ['a', 'e', 'i', 'o', 'u']:
                guesses-=2
                print("Oops! That letter is not in my word: " , get_guessed_word(secret_word, letters_guessed))
                print("_________________________________________________")
            else:
                guesses -= 1
                print("Oops! That letter is not in my word: " , get_guessed_word(secret_word, letters_guessed))
                print("____________________________________")
        
        if guesses == 0:
            print("Sorry, You ran out of guesses. The word was " + secret_word + ".")

if __name__ == "__main__":
    pass

secret_word = choose_word(wordlist)

# Want to Run Code without Hint i.e., Module 3 of Problem Set,Run the Below Line and Comment the Next Line.
#hangman (secret_word)
# Want to Run Code with Hint i.e., Module 4 of Problem Set,Run the Below Line and Comment the above Line.
hangman_with_hints(secret_word)
