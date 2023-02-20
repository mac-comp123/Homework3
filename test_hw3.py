# ====================================================================
#
#  Homework 3 tests
#  <put your name here>
# ====================================================================

# If needed, change the filename below to match your solution file's name

from hw3Code import *

# ==========================================================================================
# Testing main program

def runTests():
    """Calls testing functions"""
    test_identifyUFO()

    # test_pigLatin()

    test_alphabeticOrder()

# ==========================================================================================
# Tests for identifyUFO

def test_identifyUFO():
    """Test the identifyUFO function."""
    print()
    print("--------------------------------------")
    print("Testing identifyUFO")

    res = identifyUFO(True, 200, True)
    assert res == "It's a very smart bird."

    res = identifyUFO(True, 900, True)
    assert res == "It's a very smart bird."

    res = identifyUFO(True, 200, False)
    assert res == "It's a bird."

    res = identifyUFO(True, 201, False)
    assert res == "It's a plane."

    res = identifyUFO(True, 500.5, False)
    assert res == "It's a plane."

    res = identifyUFO(True, -0.7, False)
    assert res == "It's a bird going backwards."

    res = identifyUFO(True, -90, False)
    assert res == "It's a bird going backwards."

    res = identifyUFO(False, 200, True)
    assert res == "It's Lieutenant Pete 'Maverick' Mitchell."

    res = identifyUFO(False, -200, True)
    assert res == "It's Lieutenant Pete 'Maverick' Mitchell."

    res = identifyUFO(False, 10, False)
    assert res == "It's Superman!"

    res = identifyUFO(False, -10, False)
    assert res == "It's Superman!"

    print("    All assertions passed")


# ==========================================================================================
# Tests for pigLatin

# put the test_piglatin function here


# ==========================================================================================
# Tests for alphabeticOrder


def test_alphabeticOrder():
    """Tests the alphabeticOrder function """
    print()
    print("--------------------------------------")
    print("Testing alphabeticOrder")

    w1 = alphabeticOrder("abcdefghijklmnopqrstuvwxyz")
    assert w1 == ['abcdefghijklmnopqrstuvwxyz']

    w2 = alphabeticOrder("zyxwvutsrqponmlk")
    assert w2 == []

    w3 = alphabeticOrder("")
    assert w3 == []

    w4 = alphabeticOrder("abcdefg gfedcba dad add fad ads")
    assert w4 == ["abcdefg",  "add" , "ads"]

    w5 = alphabeticOrder("abhors, almost, begins, biopsy, chimps and chintz")
    assert w5 == ["abhors", "almost", "begins", "biopsy", "chimps", "chintz"]

    w6 = alphabeticOrder("abcdefg.gfedcba dad add! fad? ads...")
    assert w6 == ["add", "ads"]

    print("    All assertions passed")


if __name__ == '__main__':
    runTests()
