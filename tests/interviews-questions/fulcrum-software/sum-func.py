# multifunction with addition call
def sum_func(num = None, res = 0):
    if num == None:
        return res
    res += num
    return lambda num = None, res = res: sum_func(num, res)
    
print(sum_func(1)(2)(5)(10)())

# solution with using class
class sum_num (object):
    def __init__(self, val):
        self.val =val

    def __call__(self, val):
        self.val += val
        return self

    def __int__(self):
        return int(self.val)

print(int(sum_num(1)(2)(5)(10)))