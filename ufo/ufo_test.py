"""
This script unit tests the function in the associated script

@author: Amin Alhashim (aalhashi@macalester.edu)
@author: Susan Fox
"""

from ufo import *


def test_identify_ufo() -> None:
    res = identify_ufo(True, 200, True)
    assert res == "It's a very smart bird."

    res = identify_ufo(True, 900, True)
    assert res == "It's a very smart bird."

    res = identify_ufo(True, 200, False)
    assert res == "It's a bird."

    res = identify_ufo(True, 201, False)
    assert res == "It's a plane."

    res = identify_ufo(True, 500.5, False)
    assert res == "It's a plane."

    res = identify_ufo(True, -0.7, False)
    assert res == "It's a bird going backwards."

    res = identify_ufo(True, -90, False)
    assert res == "It's a bird going backwards."

    res = identify_ufo(False, 200, True)
    assert res == "It's Lieutenant Pete 'Maverick' Mitchell."

    res = identify_ufo(False, -200, True)
    assert res == "It's Lieutenant Pete 'Maverick' Mitchell."

    res = identify_ufo(False, 10, False)
    assert res == "It's Superman!"

    res = identify_ufo(False, -10, False)
    assert res == "It's Superman!"
