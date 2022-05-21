#!/usr/bin/env python

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def launch_game(game, game_counts = 3):
    name = welcome_user()
    _, game_conditions = game()
    print(game_conditions)

    for i in range(game_counts):
        questions_and_answers, _ = game()
        print('Question:', questions_and_answers[0])
        user_answer = prompt.string('Your answer: ')
        if user_answer != questions_and_answers[1]:
            print(f"'{user_answer}' is wrong answer ;(. \
            Correct answer was' '{questions_and_answers[1]}'.")
            print(f"Let's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f"Congratulations, {name}!")
