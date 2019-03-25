#!/usr/bin/python3.5
def decomposer(n, remain):
    print(n, remain)
    if remain == 0:
        return [n]
    for i in range(n-1, 0, -1):
        if (remain - pow(i, 2)) >= 0:
            r = decomposer(i, remain-pow(i, 2))
            if r:
                r.append(n)
                print('r: ', r)
                return r
    return None

def decompose(n):
    if n < 1:
        return None
    res = decomposer(n, pow(n, 2))
    # print(res[:-1])
    return res[:-1] if res else None
# decompose(10)
decompose(11)
decompose(8)
# decompose(50)