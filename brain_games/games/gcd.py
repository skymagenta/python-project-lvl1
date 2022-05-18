#!/usr/bin/env python

from random import randint


def get_greatest_common_divisor(x, y):
    """
    Находит наибольший общий делитель для двух целых положительных чисел.
    """
    for num in range(min(x, y), 0, -1):
        if (x % num == 0) and (y % num == 0):
            gcd = num
            break
    return gcd


def gcd(game_count = 3):
    questions = []
    correct_answers = []
    for i in range(game_count):
        x = randint(1, 100)
        y = randint(1, 100)
        questions.append(f"{x} {y}")
        correct_answers.append(str(get_greatest_common_divisor(x, y)))

    print('Find the greatest common divisor of given numbers.')
    return questions, correct_answers
