from implementing_a_deque import Deque

def pal_checker(a_string):
    char_deque = Deque()

    for character in a_string:
        char_deque.add_rear(character)

    still_equal = True
    
    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            still_equal = False
        
    return still_equal


