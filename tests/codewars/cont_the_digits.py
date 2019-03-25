#!/usr/bin/python3.5

def nb_dig(n, d):
    # n_list = [str(i**2) for i in range(n+1)]
    # for i in n_list:
    #     count += i.count(str(d))
    count = sum(i.count(str(d)) for i in [str(i**2) for i in range(n+1)])
    print(count)
    return count

nb_dig(10,1)