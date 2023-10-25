import pytest
import main
# import unittest

# import unittest
# import contextlib




def test_plan():
    assert "Chinese Food" 
def test_dish():
    assert "price"

def test_drink():
    assert "Beer"

def test_select_plan():
    main.user_number = "1"
    assert main.plan1["menu"]


def test_select_dish():
    main.user_dish = "2"
    assert main.dish2["menu"] 

def test_select_drink():
    main.user_dish = "3"
    assert main.drink3["menu"]


if __name__ == '__main__':
    unittest.main()