#!/usr/bin/env python

from random import randint


def even():
    game_conditions = 'Answer "yes" if the number is even, otherwise answer "no".'
    questions_and_answers = []
    x = randint(1, 100)
    questions_and_answers.append(x)
    if x % 2 == 0:
        questions_and_answers.append('yes')
    else:
        questions_and_answers.append('no')
    return questions_and_answers, game_conditions
