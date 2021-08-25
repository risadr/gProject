while True:
    try:
        iter_str = input('Take in numbers, e.g. 1, 2, 3, 4, 5, 6: ')
        iter_str = iter_str.split(', ')
        iter_int = []
        for i in iter_str:
            iter_int.append(int(i))
            if (type(int(i)) != int):
                raise ValueError
        print(f'A series of numbers you typed was: {iter_int}')
    except ValueError:
        print('Wrongly type, please type integers only！')
    else:
        #Step 1: setting up your repository with a python file.
        #(1)Write a python function that find a missing number in a list
        range_A = range(min(iter_int), max(iter_int)+1)
        list_A = list(range_A)

        def miss_num_func(iter_int):
          list_B = list(set(list_A).difference(set(iter_int)))
          ###https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/372678/
          return list_B

        miss = miss_num_func(iter_int)
        miss = sorted(miss)
        print(miss)

        if len(miss) == 1:
            print(f'There is one missing number: {miss}.')
        elif len(miss) > 1:
            print(f'There are multiple missing numbers: {miss}.')
        elif len(miss) == 0:
            print('There is no missing number.')
        break
