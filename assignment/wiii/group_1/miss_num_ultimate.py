#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script will return the missing items in a list
"""
import numpy as np

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

    item = []
    for i in range(len(lis_dif)):
        item.append(compare[lis_dif[i]])

    return item


def find_miss_num_func():
    a = input("Take in numbers(press space key to space number, ex: 0 1 2 3 4)\nEnter here: ")
    # create a list of the input numbers
    a_split = a.split(sep=' ')
    a_list = sorted(map(int, a_split))


    #find miss number with miss_num_func
    miss = miss_num_func(a_list)

    miss_to_str = ' '.join(map(str, miss))
    if len(miss) != 1:
        print("There are multilple missing numbers: %s" % miss_to_str )

    elif len(miss) == 1:
        print("There is one missing number: %s" % miss_to_str)

if __name__ == '__main__':
    find_miss_num_func()
