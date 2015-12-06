def minimum_number_quadratic(list):
    
    overall_minimum = list[0]
 
    for item1 in list:
        is_smallest = True
        for item2 in list:
            if item1 > item2:
                is_smallest = False
        if is_smallest:
            overall_minimum = item1
    return overall_minimum


def minimum_number_linear(list):
    
    minimum = list[0]
    
    for item in list:
        if item < minimum:
            minimum = item
    return minimum
