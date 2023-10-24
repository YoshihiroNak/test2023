# from main import main, plans,user, chinese_food, mexicon_food, thai_food
# import sys
# import pyfiglet
# import colorama
# from colorama import Fore, Back, Style

import pytest
from funcs import main, chinese_food, mexicon_food, thai_food, dessert1, dessert2, dessert3, alcohol, allergy, confirm, end
from unittest.mock import Mock

@pytest.fixture
def mock_input(mocker):
    # モックされた input 関数を作成します
    return mocker.patch('builtins.input', side_effect=['1', '1', 'y', 'n', 'y', '1', 'n', 'y', 'n', 'n', 'n'])

def test_chinese_food(capsys, mocker, mock_input):
    mocker.patch('catering_app.price', [])
    main()
    out, _ = capsys.readouterr()
    assert "Chicken Fried Rice" in out

def test_mexican_food(capsys, mocker, mock_input):
    mocker.patch('catering_app.price', [])
    main()
    out, _ = capsys.readouterr()
    assert "Mexican Lime Chicken" in out

def test_thai_food(capsys, mocker, mock_input):
    mocker.patch('catering_app.price', [])
    main()
    out, _ = capsys.readouterr()
    assert "Thai Fried Cheiken" in out

# 同様に他の関数をテストするテストケースを記述します

if __name__ == "__main__":
    pytest.main()
