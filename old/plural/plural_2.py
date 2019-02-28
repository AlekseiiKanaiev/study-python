#!/usr/bin/python3
""" Теперь каждое правило-условие совпадения является отдельной функцией,
которая возвращает результаты вызова функции re.search()."""  
import re

def match_sxz(noun):
    return re.search('[sxz]$', noun)

def apply_sxz(noun):
    return re.sub('$', 'es', noun)

def match_h(noun):
    return re.search('[^aeioudgkprt]h$', noun)

def apply_h(noun):
    return re.sub('$', 'es', noun)

def match_y(noun):                             
    return re.search('[^aeiou]y$', noun)
       
def apply_y(noun):                             
    return re.sub('y$', 'ies', noun)

def match_default(noun):
    return True

def apply_default(noun):
    return noun + 's'

#теперь есть структура данных rules, являющаяся последовательностью пар функций (кортеж кортежей)
rules = ((match_sxz, apply_sxz),               
         (match_h, apply_h),
         (match_y, apply_y),
         (match_default, apply_default)
         )

def plural(noun):          
    for matches_rule, apply_rule in rules:     
        if matches_rule(noun):
            return apply_rule(noun)

string = input("Enter noun: ")
result = plural(string)
print (result)
