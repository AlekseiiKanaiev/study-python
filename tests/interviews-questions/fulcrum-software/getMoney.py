moneyTypes = [5000, 1000, 500, 100, 50]

def get_money(val):
    i = 0
    c = 0
    res = {}
    while len(moneyTypes) > i:
        if val >= moneyTypes[i]:
            val -= moneyTypes[i]
            c += 1
        else:
            if c:
                res[moneyTypes[i]] = c
            c = 0
            i += 1
    if res:
        return res
    else:
        raise Exception('Not enough money')

print(get_money(5))