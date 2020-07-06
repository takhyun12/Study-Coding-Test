iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

for i in iterable1:
    for j in iterable2:
        for k in iterable3:
            print(i+j+k)


import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
itertools.product(iterable1, iterable2, iterable3)