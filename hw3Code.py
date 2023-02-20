# ====================================================================
#
#  Homework 3 solutions
#  <put your name here>
# ====================================================================

# <put import statements here>

import string



# ==============================================================
# Question 1

# put your definition of identifyUFO here


# ==============================================================
# Question 2

def isNumber(myString):
    """
    Function which takes a string as input and returns True if it can be interpreted as a number.
    i.e. converted into a float (and also therefore an int)
    """
    try:
        float(myString)
        return True
    except ValueError:
        return False

# put your definition of askUFOQuestions here


# ==============================================================
# Question 3


# put your definition of pigLatin here



# ==============================================================
# Question 4

# put your definition of alphabeticOrder here



# --------------------------------------------------------------------
# Script with sample calls to functions

if __name__ == '__main__':
    print("Sample calls...")

    #------- Sample calls for question 1
    # print(identifyUFO(True, 200, True))
    # print(identifyUFO(True, -0.7, False))
    # print(identifyUFO(False, 200, True))
    # print(identifyUFO(False, 10, False))


    #------- Sample call for question 2
    # print(askUFOQuestions())

    #------- Sample calls for question 3
    # print('dog', pigLatin("dog"))
    # print('triple', pigLatin('triple'))
    # print('anvil', pigLatin('anvil'))
    # print('velveteen', pigLatin('velveteen'))
    # print('yet', pigLatin('yet'))
    # print('myth', pigLatin('myth'))
    # print('cwm', pigLatin('cwm'))

    #------- Sample calls for question 4
    # print(alphabeticOrder("abcdefg gfedcba dad add fad ads"))
    # print(alphabeticOrder("abhors, almost, begins, biopsy, chimps and chintz"))
