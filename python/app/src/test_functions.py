import pytest
import functions
from unittest.mock import patch
import unittest
from unittest.mock import MagicMock
from unittest import mock


def test_plan(mocker):
    mocker.patch("functions.plan", return_value=[1])
    mocker.patch("functions.plan", return_value=["Chinese Food"])
    mocker.patch("functions.plan", return_value=[100])
    mocker.patch("functions.plan", return_value=[2])
    mocker.patch("functions.plan", return_value=["Mexican Food"])
    mocker.patch("functions.plan", return_value=[150])
    mocker.patch("functions.plan", return_value=[3])
    mocker.patch("functions.plan", return_value=["Thai Food"])
    mocker.patch("functions.plan", return_value=[200])
    mocker.patch("functions.plan", return_value=[])
    print(functions.plan())


def test_dish(mocker):
    mocker.patch("functions.dish", return_value=["1"])
    mocker.patch("functions.dish", return_value=["Crispy Fried Chicken"])
    mocker.patch("functions.dish", return_value=["0"])
    mocker.patch("functions.dish", return_value=["2"])
    mocker.patch("functions.dish", return_value=["Roasted Pork Belly"])
    mocker.patch("functions.dish", return_value=["20"])
    mocker.patch("functions.dish", return_value=["3"])
    mocker.patch("functions.dish", return_value=["Angus Beef Steak"])
    mocker.patch("functions.dish", return_value=["40"])
    mocker.patch("functions.plan", return_value=[])
    print(functions.dish()) 

def test_drink(mocker):
    mocker.patch("functions.drink", return_value=[1])
    mocker.patch("functions.drink", return_value=["Nothing"])
    mocker.patch("functions.drink", return_value=["0"])
    mocker.patch("functions.drink", return_value=[2])
    mocker.patch("functions.drink", return_value=["Beer"])
    mocker.patch("functions.drink", return_value=[20])
    mocker.patch("functions.drink", return_value=[3])
    mocker.patch("functions.drink", return_value=["Beer Wine Sake"])
    mocker.patch("functions.drink", return_value=[40])
    mocker.patch("functions.drink", return_value=[])
    print(functions.drink()) 


def test_select_plan(mocker):
    mocker.patch("functions.select_plan", return_value=[1])
    functions.user_plan = "3"
    assert functions.plan1["menu"]
    print(functions.select_plan()) 

def test_select_dish(mocker):
    mocker.patch("functions.select_dish", return_value=[2])
    functions.user_dish = "3"
    assert functions.dish2["menu"]
    print(functions.select_dish()) 

def test_select_drink(mocker):
    mocker.patch("functions.select_drink", return_value=[3])
    functions.user_drink = "3"
    assert functions.drink3["menu"]
    print(functions.select_drink()) 




