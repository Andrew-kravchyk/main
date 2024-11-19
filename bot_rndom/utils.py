import random


def get_random_file(lst):
    return random.choice(lst)


def get_lines(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines()
