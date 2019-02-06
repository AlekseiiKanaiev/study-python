#!/usr/bin/python3
""" Каждая функция следовала одному из двух шаблонов.
Все функции совпадения вызывают re.search(), а все функции замены вызывают re.sub().
Исключим шаблоны, чтобы объявление новых правил было более простым. """  

import re

def build_match_and_apply_functions(pattern, search, replace):
    """ Функция, которая динамически создает другие функции.
    Она принимает pattern, search и replace, затем определяет функцию matches_rule(),
    которая вызывает re.search() с шаблоном pattern,
    переданный функции build_match_and_apply_functions() в качестве аргумента,
    и word, который передан функции matches_rule(), которую вы определяете,
    аналогично с функцией apply.

    Подход, заключающийся в использовании значений внешних параметров внутри динамической функции
    называется замыканиями.
    
    В конце концов функция возвращает кортеж с двумя значениями, двумя функциями,
    которые вы только что создали. """

    def matches_rule(word):                                     
        return re.search(pattern, word)
    def apply_rule(word):                                       
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)         

# Правила формирования множественного числа теперь определены как кортеж кортежей строк.
# Первая строка в каждой группе — это регулярное выражение, которое вы бы использовали в re.search(),
# чтобы определить, подходит ли данное правило.
# Вторая и третья строки в каждой группе — это выражения для поиска и замены,
# которые вы бы использовали в re.sub(), чтобы применить правило и 
# преобразовать существительное во множественное число.

patterns = (
    ('[sxz]$',           '$',  'es'),
    ('[^aeioudgkprt]h$', '$',  'es'),
    ('(qu|[^aeiou])y$',  'y$', 'ies'),
# Если ни одно конкретное правило не применилось, код должен просто добавить s в конец данного слова. 
    ('$',                '$',  's'))       

# Создаем генератор списка, в который войдет результат функции - т.е. кортеж из 2 функций.
rules = [build_match_and_apply_functions(pattern, search, replace)  
         for (pattern, search, replace) in patterns]

def plural(noun):          
    for matches_rule, apply_rule in rules:     
        if matches_rule(noun):
            return apply_rule(noun)

string = input("Enter noun: ")
result = plural(string)
print (result)

