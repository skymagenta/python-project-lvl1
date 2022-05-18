#!/usr/bin/env python

from random import randint


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


def progression(game_count=3):
    questions = []
    correct_answers = []
    for i in range(game_count):
        list_of_num = create_sequence()
        position = randint(0, len(list_of_num) - 1)
        correct_answer = list_of_num[position]
        list_of_num[position] = '..'
        question = ' '.join(list_of_num)
        questions.append(question)
        correct_answers.append(correct_answer)
    print('What number is missing in the progression?')
    return questions, correct_answers
