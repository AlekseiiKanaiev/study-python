#!/usr/bin/python3
""" Обобщенная функция plural() разбирает файл с правилами. """

import re

def build_match_and_apply_functions(pattern, search, replace):  
    """ Функция не изменилась. """
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

def rules(rules_filename):
    """ Функция вызывает yield, который возвращает две функции,
    созданные динамически функцией build_match_and_apply_functions().
    Другими словами, rules() — это генератор,
    который отдаёт правила совпадения и изменения по требованию. """

    with open(rules_filename, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            
            # yield вернет результат, затем если будет возврат в эту функцию,
            # то она продолжит работу со следующей строки после yield
            yield build_match_and_apply_functions(pattern, search, replace)

def plural(noun, rules_filename='plural_rules.txt'):
    for matches_rule, apply_rule in rules(rules_filename):
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('no matching rule for {0}'.format(noun))

string = input("Enter noun: ")
result = plural(string)
print (result)

