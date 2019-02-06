#!/usr/bin/python3
""" Тестовая программа для перевода из римских чисел и обратно """

import roman1
import roman2
import unittest

class KnownValues(unittest.TestCase):
    """ Класс для теста на проверку заранее известных значений """

    known_values = ( (1, 'I'),
                    (2, 'II'),
                    (3, 'III'),
                    (4, 'IV'),
                    (5, 'V'),
                    (6, 'VI'),
                    (7, 'VII'),
                    (8, 'VIII'),
                    (9, 'IX'),
                    (10, 'X'),
                    (50, 'L'),
                    (100, 'C'),
                    (500, 'D'),
                    (1000, 'M'),
                    (31, 'XXXI'),
                    (148, 'CXLVIII'),
                    (294, 'CCXCIV'),
                    (312, 'CCCXII'),
                    (421, 'CDXXI'),
                    (528, 'DXXVIII'),
                    (621, 'DCXXI'),
                    (782, 'DCCLXXXII'),
                    (870, 'DCCCLXX'),
                    (941, 'CMXLI'),
                    (1043, 'MXLIII'),
                    (1110, 'MCX'),
                    (1226, 'MCCXXVI'),
                    (1301, 'MCCCI'),
                    (1485, 'MCDLXXXV'),
                    (1509, 'MDIX'),
                    (1607, 'MDCVII'),
                    (1754, 'MDCCLIV'),
                    (1832, 'MDCCCXXXII'),
                    (1993, 'MCMXCIII'),
                    (2074, 'MMLXXIV'),
                    (2152, 'MMCLII'),
                    (2212, 'MMCCXII'),
                    (2343, 'MMCCCXLIII'),
                    (2499, 'MMCDXCIX'),
                    (2574, 'MMDLXXIV'),
                    (2646, 'MMDCXLVI'),
                    (2723, 'MMDCCXXIII'),
                    (2892, 'MMDCCCXCII'),
                    (2975, 'MMCMLXXV'),
                    (3051, 'MMMLI'),
                    (3185, 'MMMCLXXXV'),
                    (3250, 'MMMCCL'),
                    (3313, 'MMMCCCXIII'),
                    (3408, 'MMMCDVIII'),
                    (3501, 'MMMDI'),
                    (3610, 'MMMDCX'),
                    (3743, 'MMMDCCXLIII'),
                    (3844, 'MMMDCCCXLIV'),
                    (3888, 'MMMDCCCLXXXVIII'),
                    (3940, 'MMMCMXL'),
                    (3999, 'MMMCMXCIX'))

    def test_to_roman_known_values(self):
        """ to_roman should give known result with known input """

        for integer, numeral in self.known_values:
            result = roman1.to_roman(integer)

            # сравнивает 2 значения и выводит ошибки при несовпадении
            self.assertEqual(numeral, result)

    def test_from_roman_known_values(self):
        '''from_roman should give known result with known input'''
        
        for integer, numeral in self.known_values:
            result = roman1.from_roman(numeral)
            self.assertEqual(integer, result)

class ToRomanBadInput(unittest.TestCase):
    """ Класс для теста на проверку неправильно введеных значений, в том числе меньше 1 и больше 3999 """

    def test_too_large(self):
        '''to_roman should fail with large input'''

        #  метод assertRaises, который принимает следующие аргументы:
        #  тип ожидаемого исключения, имя тестируемой функции и аргументы этой функции.
        #  (Если тестируемая функция принимает более одного аргумента, все они передаются
        #  методу assertRaises по порядку, как будто передаете их тестируемой функции.)
        #  Все что Вы делаете - говорите, какой тип исключения ожидаете (roman2.OutOfRangeError),
        #  имя функции (to_roman()), и ее аргументы (4000). Метод assertRaises позаботится о
        #  вызове функции to_roman() и проверит, что она возвращает исключение
        #  roman2.OutOfRangeError.

        self.assertRaises(roman2.OutOfRangeError, roman2.to_roman, 4000)
    
    def test_zero(self):
        self.assertRaises(roman2.OutOfRangeError, roman2.to_roman, 0)

    def test_negative(self):
        self.assertRaises(roman2.OutOfRangeError, roman2.to_roman, -1)

    def test_not_integer(self):
        self.assertRaises(roman2.NonIntegerError, roman2.to_roman, 1.5)

class FromRomanBadInput(unittest.TestCase):

    def test_too_many_repeated_numerals(self):
        '''from_roman should fail with too many repeated numerals'''

        for numeral in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(roman2.InvalidRomanNumeralError, roman2.from_roman, numeral)

    def test_repeated_pairs(self):
        '''from_roman should fail with repeated pairs of numerals'''

        for numeral in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
            self.assertRaises(roman2.InvalidRomanNumeralError, roman2.from_roman, numeral)

    def test_malformed_antecedents(self):
        '''from_roman should fail with malformed antecedents'''

        for numeral in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV', 'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(roman2.InvalidRomanNumeralError, roman2.from_roman, numeral)

class RoundtripCheck(unittest.TestCase):
    """ передает все числа из интервала [1, 3999] функции to_roman(),
    затем вызывает from_roman() и проверяет соответствие результата исходному числу """

    def test_roundtrip(self):
        for integer in range(1, 4000):
            numeral = roman1.to_roman(integer)
            result = roman1.from_roman(numeral)
            self.assertEqual(integer, result)

if __name__ == "__main__":
    unittest.main()
