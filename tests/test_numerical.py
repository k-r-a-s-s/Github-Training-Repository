'''
function test_numerical():
'''
import src.numerical
import numpy as np
import pytest

def test_bumpy_reduction():
    expected_result = pytest.approx(11.99, abs=0.1)
    assert src.numerical.bumpy_reduction(10, 20) == expected_result


def test_raises():
    with pytest.raises(NotImplementedError):
        src.numerical.bumpy_reduction(0.5, -1)
        src.numerical.bumpy_reduction(0.5, 'dogs')


