# Programming Fundamentals Lab
# Problem Set 3
# Submitted by: 2019-CE-3 (Sundas Noreen)

import math
import random
import string
import copy

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    '*': 0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3,
    'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def load_words():  # This Function returns a list of valid words.
    print("Wait!! We Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.
    sequence: string or list
    return: dictionary
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq

# Problem No 1 :- Scoring a Hand

def get_word_score(word, n):   # Returns the score for a word.
    if len(word) != 0:
        word = word.lower()
        firstComponent = 0
        for l in word:  # CHANGES NEEDED
            firstComponent += SCRABBLE_LETTER_VALUES[l]
        secondComponent = max(7 * len(word) - 3 * (n - len(word)), 1)
        score = firstComponent * secondComponent
    else:
        score = 0
    return score

def display_hand(hand):   # Displays the letters currently in the hand.
    keys = hand.keys()
    for l in keys:
        for j in range(hand[l]):
            print(l, end=' ')     # print all on the same line
    print()     # print an empty line

def deal_hand(n): # Returns a random hand containing n lowercase letters. Hands are represented as dictionaries.
    hand = {}
    num_vowels = int(math.ceil(n / 3))

    for i in range(1, num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    hand['*'] = 1
    return hand

# Problem No 2:- Update a hand by removing letters

def update_hand(hand, word):  # Uses up the letters in the given word and returns the new hand.
    keys = hand.keys()
    handCopy = copy.copy(hand)
    for letter in word.lower():
        if letter in keys:
            handCopy[letter] -= 1
            if handCopy[letter] == 0:
                del handCopy[letter]
    return handCopy

# Problem  No 3:- Test word validity

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    Found = False
    handCopy = copy.copy(hand)
    for v in VOWELS:
        tempWord = ''
        for letter in word.lower():
            if letter == '*':
                tempWord += v
            else:
                tempWord += letter
        if tempWord in word_list:
            Found = True
            break

    if Found:
        for let in word.lower():
            if let not in handCopy.keys():
                return False
            else:
                handCopy = update_hand(handCopy, let)
        return True
    else:
        return False

# Problem No 5:- Playing a hand

def calculate_handlen(hand): # Returns the length in the current hand.
    """
    hand: dictionary (string-> int)
    returns: integer
    """
    values = hand.values()
    l = list(values)
    length = sum(l)
    return length

def play_hand(hand, word_list): # Allows the user to play the given hand
    """
    * The hand is displayed.
    * The user may input a word.
    * When any word is entered (valid or invalid), it uses up letters
      from the hand.
    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
    """
    score = 0
    while calculate_handlen(hand) != 0: # As long as there are still letters left in the hand.
        print(end='Current Hand: ') # Display the hand
        display_hand(hand)
        inputWord = input('Enter word, or "!!" to indicate that you are finished: ') # Ask user for input
        if inputWord == '!!':
           break
        else:
            if is_valid_word(inputWord, hand, word_list):   # If the word is valid:
                print(end='"{0}" got score {1} points'.format(inputWord,get_word_score(inputWord, calculate_handlen(hand))))
                score += get_word_score(inputWord, calculate_handlen(hand))
                print('Total score :', score)
            else:
                print('That is not a valid word. Please choose another word ')
            hand = update_hand(hand, inputWord)

    if calculate_handlen(hand) == 0:  # Game is over (user entered '!!' or ran out of letters),
        print(end='You ran out of words. ')
    print('Total score for this hand: {0}'.format(score))
    return score

# Problem No 6:- Playing a game

def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    alphas = string.ascii_lowercase
    letters_in_hand = ''.join(list(hand.keys()))
    for let in letters_in_hand:
        alphas.replace(let, '')
    alpha = random.choice(alphas)
    hand[alpha] = hand.pop(letter)
    return hand

def play_game(word_list):  # Allow the user to play a series of hands
    """
    * Asks the user to input a total number of hands
    * Accumulates the score for each hand into a total score for the
      entire series
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.
    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep
      the better of the two scores for that hand.  This can only be done once
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.
    * Note: if you replay a hand, you do not get the option to substitute
      a letter - you must play whatever hand you just had.
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    TotalScore = 0
    num_hands = int(input('Enter total number of hands: '))
    for i in range(num_hands):
        hand = deal_hand(HAND_SIZE)
        while True:
            print(end='Current Hand: ')
            display_hand(hand)
            substitute = input('Would you like to substitute a letter? ')
            if substitute.lower() == 'yes':
                letter = input('Which letter would you like to replace: ')
                hand = substitute_hand(hand, letter)
            TotalScore += play_hand(hand, word_list)
            print('______________________________________________')
            replay = input('Would you like to replay the hand? ')
            if replay == 'yes':
                pass
            else:
                break
    print('Total score over all hands:', TotalScore)


# Build data structures used for entire session and play game.
# Do not remove the "if _name_ == '_main_':" line - this code is executed
# when the program is run directly, instead of through an import statement


if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
