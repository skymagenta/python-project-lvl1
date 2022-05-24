from random import randint

RULE = 'Answer "yes" if the number is even, \
otherwise answer "no".'


def game_round():
    x = randint(1, 100)
    question = x
    answer = 'no'
    if x % 2 == 0:
        answer = 'yes'
    return question, answer
