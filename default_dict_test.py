from collections import defaultdict

import random

pool = {"NUTCRACKER":5, "t1":5, "y1":1, "t2":1}

completion = ['NUTCRACKER']

for i in completion:
    print(i)
    if pool[i]:
        print(i)
        pool.pop(i)

#print(pool)

list1 = ['a','b','c']
list2 = ['d']

random.shuffle(list1)

print(list1)