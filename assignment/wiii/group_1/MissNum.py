<<<<<<< HEAD
<<<<<<< HEAD
#!/usr/bin/env python
# coding: utf-8
=======
"""
This file is part of the github course W2 task
"""
import numpy as np
>>>>>>> 754c5963d52b7f35ac340377aed974049123b36b

iter = [0, 1, 2, 4, 5, 6, 8, 9]
def miss_num_func(iter):
    '''
    This function takes in a list called "iter" with items in serial order,
    and returns the missing item.
    1. Make another list called "compare" with the biggest item in iter list as the final item
    2. Compare "compare" with "iter", and returns the missing item
    '''
    n = iter[-1]
    compare = np.arange(0, n+1, 1).tolist()
    same_index = []
    for i in range(len(iter)):
        for j in range(len(compare)):
            if iter[i] == compare[j]:
                same_index.append(j)
    all_index = list(range(0, n+1))
    lis_dif = [i for i in all_index if i not in same_index]

<<<<<<< HEAD
print(miss_num_funct(iter))
=======
def miss_func_num(iter):
    return [x for x in range(lst[0], lst[-1]+1)
                               if x not in iter]

# Driver code
iter = [0, 1, 2, 4, 5, 6]
miss = miss_func_num(iter)
for i in miss:
    print(i)
#print(miss)
>>>>>>> 1a0e1ec27b773629fa1e3a38e16f7d321aebc87b
=======
    item = []
    for i in range(len(lis_dif)):
        item.append(compare[lis_dif[i]])

    return item

miss = miss_num_func(iter)

miss
>>>>>>> 754c5963d52b7f35ac340377aed974049123b36b
