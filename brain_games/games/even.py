#!/usr/bin/env python

from random import randint


def even(game_count=3):
    questions = []
    correct_answers = []
    for i in range(game_count):
        x = randint(1, 100)
        questions.append(str(x))

        if x % 2 == 0:
            correct_answers.append('yes')
        else:
            correct_answers.append('no')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return questions, correct_answers
