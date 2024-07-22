from reassesslib import utils
import pytest


def test_negative_number():
    for i in range(10):
        with pytest.raises(ValueError):
            utils.random_draw(-5*i)


def test_odd_number():
    for i in range(10):
        with pytest.raises(ValueError):
            utils.random_draw(2*i+1)


def test_nonInt():
    for i in range(1, 11):
        with pytest.raises(ValueError):
            utils.random_draw(float(2*i))
