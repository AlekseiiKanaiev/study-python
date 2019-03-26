#!/usr/bin/python3.5

def Descending_Order(num):
    if num<0:
        return 'error'
    result = [n for n in str(num)]
    result.sort(reverse = True)
    print (int(''.join(result)))

    print (int("".join(sorted(str(num), reverse=True))))

    return result

Descending_Order(545456)
Descending_Order(784512)

