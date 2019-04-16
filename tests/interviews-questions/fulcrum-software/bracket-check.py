def bracket_check(str):
    c = 0
    for i in str:
        if i == '(': c += 1
        elif i == ')': c -= 1
    return c == 0

s = '(sadklasfk(sadasda(sadasd)))'
print(bracket_check(s))