list1 = [1, 2, 3, 4, 5]
list2 = ['one', 'two', 'tree', 'four', 'five', 'six']
d = {}
for i in range(len(list1)):
    if i >= len(list2):
        d[list1[i]] = None
    else:
        d[list1[i]] = list2[i]
# d = dict(zip(list1, list2))
print(d)