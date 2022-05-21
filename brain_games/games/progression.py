#!/usr/bin/env python

from random import randint


def create_sequence():
    """
    Creates a list of 10 numbers ranging from 1 to 99
    in an arithmetic progression.
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
    game_conditions = 'What number is missing in the progression?'
    questions_and_answers = []
    list_of_num = create_sequence()
    position = randint(0, len(list_of_num) - 1)
    correct_answer = list_of_num[position]
    list_of_num[position] = '..'
    question = ' '.join(list_of_num)
    questions_and_answers.append(question)
    questions_and_answers.append(correct_answer)
    return questions_and_answers, game_conditions
