#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

def test_if_equal(a, b):
    assert a == b, "a[{0}] is not equal to b[{1}]".format(a, b)
    
if __name__ == "__main__":
    test_if_equal(2, 3)
    test_if_equal(1, 1)
