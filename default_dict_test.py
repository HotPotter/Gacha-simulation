from collections import defaultdict

pool = {"NUTCRACKER":5, "t1":5, "y1":1, "t2":1}

completion = ['NUTCRACKER']

for i in completion:
    print(i)
    if pool[i]:
        print(i)
        pool.pop(i)

print(pool)