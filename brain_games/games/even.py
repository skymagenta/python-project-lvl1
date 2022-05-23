#!/usr/bin/env python

from random import randint

GAME_CONDITIONS = 'Answer "yes" if the number is even, \
otherwise answer "no".'


def game():
    x = randint(1, 100)
    question = x
    answer = 'no'
    if x % 2 == 0:
        answer = 'yes'
    return question, answer
