import time

def sum_of_n(n):
    start = time.time()

    the_sum = 0
    for i in range(1, n+1):
        the_sum += i

    end = time.time()
    
    return the_sum, end - start


def sum_of_n3(n):
    start = time.time()

    the_sum = (n*(n+1))/2
    
    end = time.time()
    
    return the_sum, end - start
