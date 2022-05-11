#!/usr/bin/env python

from random import randint
import prompt


def create_sequence():
    """
    Создает список из 10 чисел в диапазоне от 1 до 99,
    образующих арифметическую прогрессию.
    """
    first_element = randint(1, 29)
    step = randint(2, 7)
    list_of_num = []
    max_elements = 10
    added_element = first_element
    for i in range(max_elements):
        list_of_num.append(str(added_element))
        added_element += step

    return list_of_num


def progression():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello', name, '!')
    print('What number is missing in the progression?')

    i = 0

    while i < 3:
        list_of_num = create_sequence()
        position = randint(0, len(list_of_num) - 1)
        correct_answer = list_of_num[position]
        list_of_num[position] = '..'
        str_for_user = ' '.join(list_of_num)
        print('Question:', str_for_user)
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(answer, 'is wrong answer ;(. Correct answer was',
                  correct_answer, '.')
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
        i += 1

    if i == 3:
        print(f'Congratulations, {name}!')
