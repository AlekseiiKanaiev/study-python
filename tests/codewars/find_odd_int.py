def find_odd(arr):
    c = 0
    r = 0
    t = [i for i in set(arr) if arr.count(i) > c and arr.count(i) % 2 != 0].pop()
    print(t)
    for i in set(arr):
        if arr.count(i) > c and arr.count(i) % 2 != 0:
            c = arr.count(i)
            r = i
    return r
    # return [i for i in set(arr) if arr.count(i) % 2 != 0].pop()

print(find_odd([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))