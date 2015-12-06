## Hill climbing version of random monkey algorithm.

import random

alphabet = "abcdefghijklmnopqrstuvwxyz "
shakespeare = "methinks it is like a weasel"

def random_char_generator():
    return random.choice(alphabet)

def compare_chars(char1, char2):
    return char1 == char2

def generate_and_score():
    best_sentence_so_far = ""
    number_of_tries = 0
    current_index = 0    
    while current_index < len(shakespeare):
        random_char = random_char_generator()
        if compare_chars(random_char, shakespeare[current_index]):
            best_sentence_so_far += random_char
            current_index += 1
            print(best_sentence_so_far)
        number_of_tries += 1
    print("It only took " + str(number_of_tries) + " tries!")

generate_and_score()
