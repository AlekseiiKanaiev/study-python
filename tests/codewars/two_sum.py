#!/usr/bin/python3.5

def two_sum(numbers, target):
    # start coding!
    print(numbers)
    for i in range(len(numbers)):
        for j in range(1 + i, len(numbers)):
            if numbers[i]+numbers[j] == target:
                print(1)
                return [i, j]
    return 0


two_sum([1,2,3], 4)