import timeit
import random


## 1. Devise an experiment to verify that the list index operator is O(1)

for i in range(10000, 1000001, 20000):
    t = timeit.Timer("x[(random.randrange(%d))]"%i,
                     "from __main__ import random, x")

    x = list(range(i))
    index_time = t.timeit(number=1000)
    print("%d, %10.4f" % (i, index_time))


## 2. Devise an experiment to verify that get item and set item are O(1) for 
##    dictionaries.

for i in range(10000, 1000001, 20000):
    set_dict = timeit.Timer("x[(random.randrange(%d))]"%i,
                            "from __main__ import random, x")
    
    get_dict = timeit.Timer("x.get(random.randrange(%d))"%i,
                            "from __main__ import random, x")

    x = {j:None for j in range(i)}

    set_time = set_dict.timeit(number=1000)
    get_time = get_dict.timeit(number=1000)
    print("%d, %10.4f, %10.4f" % (i, get_time, set_time))


## 3. Devise an experiment that compares the performance of the del operator on 
##    lists and dictionaries.

for i in range(10000, 2000001, 20000):
    test_list = timeit.Timer("del x[(random.randrange(%d))]"%i,
                             "from __main__ import random, x")

    test_dict = timeit.Timer("del x2[(random.randrange(%d))]"%i,
                             "from __main__ import random, x2")

    x = list(range(i))
    x2 = {j:None for j in range(i)}

# Number set to 1, since can't repeat deletion of same index without getting error.
# Unfortunately, this means more variance in run time numbers, since no averaging.
    list_del_time = test_list.timeit(number=(1))
    dict_del_time = test_dict.timeit(number=(1))
    print("%d, %10.4f, %10.4f" % (i, list_del_time, dict_del_time))


## 4. Given a list of numbers in random order, write an algorithm that works in 
##    O(nlog(n)) to find the kth smallest number in the list.

def smallest_in_list_nlogn(lst):
# The built-in list.sort() method is a merge sort that works in O(n log(n)). 
    lst.sort()
    return lst[0]


## 5. Can you improve the algorithm from the previous problem to be linear? Explain.

def smallest_in_list_n(lst):

    smallest = lst[0]
    for i in lst:
        if smallest > i:
            smallest = i
    return smallest

# This function improves upon the previous algorithm since it is a linear solution.
# It only iterates through a list of n items once, checking to see if each item is
# smaller than a variable set to the lowest item encountered so far.
# The algorithm doesn't have to account for the order of each item in relation to 
# the others, due to only looking for the lowest item, so it can be "optimized".


