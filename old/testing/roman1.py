#!/usr/bin/python3
""" функция перевода из циферных чисел в римские """

# Уникальные значения римских чисел, выставлены по порядку в сторону уменьшения.
roman_numeral_map = (('M', 1000),
                ('CM', 900),
                ('D', 500),
                ('CD', 400),
                ('C', 100),
                ('XC', 90),
                ('L', 50),
                ('XL', 40),
                ('X', 10),
                ('IX', 9),
                ('V', 5),
                ('IV', 4),
                ('I', 1))

def to_roman(n):
    '''convert integer to Roman numeral'''
    #pass применяется в качестве заглушки
    # pass

    result = ''

    #  Для конвертирования в римское число необходимо просто пройти в цикле roman_numeral_map,
    #  находя наименьшее число, в которое влезает остаток ввода.
    #  При нахожднии такового, к возвращаемому значению функции добавляется соответствующее 
    #  римское представление, ввод уменьшается на это число и далее операция повторяется
    #  для следующего кортежа.
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    return result

def from_roman(roman):
    '''convert numeral from Roman to integer '''

    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        
        # нарезаем римское число ака[1:2]
        while roman[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result