#!/usr/bin/python3

# 1. Bagels Project ##

# A deductive logic game where you must guess a number based on clues.
import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    # Game intro
    print('''Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com
    
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:    That means:
      Pico         One digit is correct but in the wrong position.
      Fermi        One digit is correct and in the right position.
      Bagels       No digit is correct.
    
    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.'''.format(NUM_DIGITS))

   # Game loop
    while True:
        # Our secret number
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        # Guess it!
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''

            # What is the guess?
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            # print clues
            clues = getClues(guess, secretNum)
            print(clues)
            
            # next guess
            numGuesses += 1

            if guess == secretNum:
                break

            if numGuesses > MAX_GUESSES:
                print('You ran out of your guesses.')
                print('The answer was {}'.format(secretNum))

        # Do you want to play again?
        print('Do you want to play again? (yes or no)')
        
        # wow checking
        if not input('> ').lower().startswith('y'):
            break

    print('Thanks for playing!')


# Get secret number
def getSecretNum():
    # generate random {NUM_DIGITS} ko number
    secretNum = ''

    numbers = list('0123456789')
    random.shuffle(numbers)

    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])

    return secretNum

# Get clues
def getClues(guess, secretNum):
    # Return 'pico, fermi, bagels clues for a guess of the secret number'

    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')

        elif guess[i] in secretNum:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'
    else:
        # Sorting clues to making it hard!
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()
