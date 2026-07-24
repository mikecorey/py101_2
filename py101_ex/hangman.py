# Hangman game
# intentionally broken right now!!!

MAX_GUESSES = 10

answer = "Four Score and seven years ago"

answer = answer.lower()

letters = 'abcdefghijklmnopqrstuvwxyz'

guessed_letters = set()

while len(guessed_letters) < MAX_GUESSES:
    # Display Board
    print(f'Attempt {len(guessed_letters)}')
    print(f'Already Guessed: {guessed_letters}')
    gameboard = ''
    for c in answer:
        if c == ' ':
            gameboard += ' '
        elif c in guessed_letters:
            gameboard += c
        else:
            gameboard += '_'
    print(gameboard)

    # Get Letter from user
    guess = input("Enter a letter: ")
    guessed_letters.add(guess[0])

    # Check win condition
    if guessed_letters == set(answer) - {' '}:
        print("YOU WIN!!!")
        gameboard = ''
        for c in answer:
            if c == ' ':
                gameboard += ' '
            elif c in guessed_letters:
                gameboard += c
            else:
                gameboard += '_'
        print(gameboard)
        break

if len(guessed_letters) >= MAX_GUESSES:
    print("You Lose!!!")
