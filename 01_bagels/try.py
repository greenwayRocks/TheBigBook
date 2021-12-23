#! /usr/bin/python3

# Bagels game !! Input guess, check if it is the secretNum, give clues until you run out of guesses.
import random


def main():
    while True: # main game loop

        maxGuesses = 10
        numGuesses = 1
        num_digits = 3

        secretNum = getSecretNum(num_digits)

        # welcome
        print('Welcome. Out of {} guesses, find out the secret number. You will have clues'.format(maxGuesses))

        # input until 10 valid guesses
        while numGuesses <= maxGuesses:
            if not len(guess) == num_digits or not guess.isdecimal():
                print('\nGuess[{}]: '.format(numGuesses))
                guess = input('> ')

            numGuesses += 1

            if guess == secretNum:
                print('You got it!')
                break # break out
            else:
                clues = getClues(guess, secretNum)
                print(clues)

            if numGuesses > maxGuesses:
                print("You have run out of guesses!")
                print("The answer was {}".format(secretNum))

        print('\nDo you want to play again(y/n)? ')
        
        # nice condition
        if not input('> ').lower().startswith('y'):
            break

    print('Thanks for playing')

# Utilities
def getSecretNum(num_digits):
    secretNum = ''

    numbers = list('0123456789')
    random.shuffle(numbers)

    for i in range(num_digits):
        secretNum += str(numbers[i])
    
    return secretNum

def getClues(guess, secretNum):
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')

    if len(clues) == 0:
        return '## Bagels ##'
    else:
        return ' '.join(clues)

if __name__ == '__main__':
    main()
