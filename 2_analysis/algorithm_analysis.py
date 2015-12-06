import timeit
import random


## 1. Devise an experiment to verify that the list index operator is O(1)

for i in range(10000, 1000001, 20000):
    t = timeit.Timer("x[(random.randrange(%d))]"%i,
                     "from __main__ import random, x")

    x = list(range(i))
    index_time = t.timeit(number=1000)
    print("%d, %10.4f" % (i, index_time))


## 2. Devise an experiment to verify that get item and set item are O(1)
##    for dictionaries.

for i in range(10000, 1000001, 20000):
    set_dict = timeit.Timer("x[(random.randrange(%d))]"%i,
                            "from __main__ import random, x")
    
    get_dict = timeit.Timer("x.get(random.randrange(%d))"%i,
                            "from __main__ import random, x")

    x = {j:None for j in range(i)}

    set_time = set_dict.timeit(number=1000)
    get_time = get_dict.timeit(number=1000)
    print("%d, %10.4f, %10.4f" % (i, get_time, set_time))


## 3. Devise an experiment that compares the performance of the del
##    operator on lists and dictionaries.

for i in range(10000, 1000001, 20000):
    test_list = timeit.Timer("del x[(random.randrange(%d))]"%i,
                             "from __main__ import random, x")

    test_dict = timeit.Timer("del x2[(random.randrange(%d))]"%i,
                             "from __main__ import random, x")

    x = list(range(i))
    x2 = {j:None for j in range(i)}

    list_del_time = test_list.timeit(number=1000)
    dict_del_time = test_dict.timeit(number=1000)
    print("%d, %10.4f, %10.4f" % (i, list_del_time, dict_del_time))

