keys = [['1'], ['A', 'B', 'C', '2'], ['D', 'E', 'F', '3'], ['G', 'H', 'I', '4'],['J', 'K', 'L', '5'],\
         ['M', 'N', 'O', '6'], ['P' , 'Q', 'R', 'S', '7'], ['T', 'U', 'V', '8'],\
         ['W', 'X', 'Y', 'Z', '9'], [' ', '0'], ['*'], ['#']]

keys_s = ['1', 'ABC2', 'DEF3',\
         'GHI4', 'JKL5', 'MNO6',\
         'PQRS7', 'TUV8', 'WXYZ9',\
         '*', ' 0', '#']

def presses(s):
    count = 0
    for let in s.upper():
        r = [el.index(let)+1 for el in keys if let in el]
        if r:
            count += r.pop()
    return count

def presses2(s):
    return sum([el.find(let)+1 for let in s.upper() for el in keys_s if let in el ])

# l = [['A', 'B', 'C', 2], ['D', 'E', 'F', 3], ['G', 'H', 'I', 4],['J', 'K', 'L', 5],\
#          ['M', 'N', 'O', 6], ['P' , 'Q', 'R', 'S', 7], ['T', 'U', 'V', 8],\
#          ['W', 'X', 'Y', 'Z', 9], [' ', 0]]
# s = 'L'
# r = [let.index(s)+1 for let in l if s in let].pop()

# print(r)

print(presses('LOL'))
print(presses2('LOL'))