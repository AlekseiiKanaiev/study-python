def get_primes(n):
    res = [2]
    for i in range(2, n+1):
        if all(map(lambda x: i % x, res)):
            res.append(i)
    return res
print(get_primes(25))