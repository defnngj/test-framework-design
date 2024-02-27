"""
test_sample_3.py
nose2例子
"""
from nose2.tools import params


@params("Sir Bedevere", "Miss Islington", "Duck")
def test_is_knight(value):
    assert value.startswith('Sir')
