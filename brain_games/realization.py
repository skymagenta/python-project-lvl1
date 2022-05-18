#!/usr/bin/env python

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def machinarium(game):
    name = welcome_user()
    questions, correct_answers = game()
    correct_answers_counts = 0

    for i in range(len(questions)):
        print('Question:', questions[i])
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answers[i]:
            correct_answers_counts += 1
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. \
            Correct answer was' {correct_answers[i]}.")
            print(f"Let's try again, {name}!")
            break
    if correct_answers_counts == len(questions):
        print(f"Congratulations, {name}!")
