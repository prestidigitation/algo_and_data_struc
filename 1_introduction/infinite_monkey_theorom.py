import random

alphabet = "abcdefghijklmnopqrstuvwxyz "
shakespeare = "methinks it is like a weasel"

def randomLetterSequence():
    sequence = ""
    for i in range(28):
        sequence += random.choice(alphabet)
    return sequence

def equalityTester(randomSentence, notRandomSentence):
    return(randomSentence == notRandomSentence)

def numberCruncher():
    areTheyEqual = False
    number_of_tries = 0
    while areTheyEqual is False:
        blah = randomLetterSequence()
        if equalityTester(blah, shakespeare) is True:
            areTheyEqual = True
            return(number_of_tries)


