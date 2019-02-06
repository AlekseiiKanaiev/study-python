#!/usr/bin/python3
""" Программа в функции plural ищет окончание слова и
    подставляет соответствующее окончание во мн. числе,
    используя регулярные выражения"""  
import re

def plural(noun):
    #Если слово оканчиваеться на sxz
    if re.search('[sxz]$', noun):     
        #то подствить окончание es        
        return re.sub('$', 'es', noun)
    #если перед h, которая стоит в конце, стоит НЕ aeioudgkprt         
    elif re.search('[^aeioudgkprt]h$', noun):
        #то подствить окончание es 
        return re.sub('$', 'es', noun)      
    #если перед y, которая стоит в конце, стоит НЕ aeiou  
    elif re.search('[^aeiou]y$', noun): 
        #то подствить вместо y окончание ies     
        return re.sub('y$', 'ies', noun)    
    else:
        return noun + 's'

string = input("Enter noun: ")
result = plural(string)
print (result)

