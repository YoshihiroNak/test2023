import main
import pytest
from unittest.mock import patch

def test_end(mocker):
    mocker.patch("main.end", return_value= "y")
    mocker.patch("main.end", return_value= "n")
    mocker.patch("main.end", return_value= "")
    mocker.patch("main.end", return_value= "0")
    print(main.end())

