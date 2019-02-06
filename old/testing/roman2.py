#!/usr/bin/python3
""" Продолжени функцияи перевода из циферных чисел в римские """

def to_roman(integer):
    '''convert integer to Roman numeral'''
    #pass применяется в качестве заглушки
    # pass

    if not (1 < integer < 4000):
        raise OutOfRangeError('number out of range (must be between 1 and 4000)')

    # isinstance определяет принадлежит ли переменная типу
    if not isinstance(integer, int):
        raise NonIntegerError('non-integers can not be converted') 
      
def from_roman(numeral):
    pass

class OutOfRangeError(ValueError):
    pass
class NonIntegerError(ValueError):
    pass
class InvalidRomanNumeralError(ValueError):
    pass