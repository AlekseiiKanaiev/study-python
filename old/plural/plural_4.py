#!/usr/bin/python3
""" Возьмем правила и расположим их в отдельном файле - plural_rules.txt,
где они могут поддерживаться отдельно от использующего их кода
Никаких сложных структур данных, просто разделенные на три колонки данные.
Сделанное улучшение заключается в том, что вы полностью вынесли правила во внешний файл,
так что он может поддерживаться отдельно от использующего его кода. """

import re

def build_match_and_apply_functions(pattern, search, replace):  
    """ Функция не изменилась. """
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

# Подготавливаем пустой список. 
rules = []

# Открываем файл и считываем строки. 
with open('plural_rules.txt', encoding='utf-8') as pattern_file:  
    for line in pattern_file:    
        # Каждая строка в файле содержит три значения, но они разделены пустым пространством
        # (табуляцией или пробелами, без разницы).
        # Чтобы разделить их, используем строковый метод split().
        # Первый аргумент для split() — None, что означает
        # «разделить любым символом свободного пространства (табуляцией или пробелом, без разницы)».
        # Второй аргумент — 3, что означает «разбить свободным пространством 3 раза,
        # затем оставить остальную часть строки»
        # Строка вида «[sxz]$ $ es» будет разбита и преобразована в список ['[sxz]$', '$', 'es'],
        # что означает что pattern станет '[sxz]$', search — '$', а replace получит значение 'es'.                                  
        pattern, search, replace = line.split(None, 3)

        # Передаем pattern, search и replace функции build_match_and_apply_function(),
        # которая возвращает кортеж функций. Добавляем этот кортеж в список rules. 
        rules.append(build_match_and_apply_functions(              
                pattern, search, replace))

def plural(noun):          
    for matches_rule, apply_rule in rules:     
        if matches_rule(noun):
            return apply_rule(noun)

string = input("Enter noun: ")
result = plural(string)
print (result)

