#!/usr/bin/env python

import prompt


def launch_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game.GAME_CONDITIONS)

    GAME_COUNTS = 3

    for i in range(GAME_COUNTS):
        question, answer = game.game()
        print('Question:', question)
        user_answer = prompt.string('Your answer: ')
        if user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f"Congratulations, {name}!")
