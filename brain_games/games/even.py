from random import randint

RULE = 'Answer "yes" if the number is even, \
otherwise answer "no".'


def game_round():
    question = randint(1, 100)
    answer = 'no'
    if question % 2 == 0:
        answer = 'yes'
    return question, answer
