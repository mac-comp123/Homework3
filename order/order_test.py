"""
This script unit tests the function in the associated script

@author: Amin Alhashim (aalhashi@macalester.edu)
@author: Susan Fox
"""

from order import *


def test_alphabetic_order():
    w1 = alphabetic_order("abcdefghijklmnopqrstuvwxyz")
    assert w1 == ['abcdefghijklmnopqrstuvwxyz']

    w2 = alphabetic_order("zyxwvutsrqponmlk")
    assert w2 == []

    w3 = alphabetic_order("")
    assert w3 == []

    w4 = alphabetic_order("abcdefg gfedcba dad add fad ads")
    assert w4 == ["abcdefg", "add", "ads"]

    w5 = alphabetic_order("abhors, almost, begins, biopsy, chimps and chintz")
    assert w5 == ["abhors", "almost", "begins", "biopsy", "chimps", "chintz"]

    w6 = alphabetic_order("abcdefg.gfedcba dad add! fad? ads...")
    assert w6 == ["add", "ads"]
