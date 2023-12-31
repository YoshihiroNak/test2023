#!/bin/bash
if ! [[ -x "$(command -v python3)" ]];
then
    echo "Error:
        You don't have Python. You need to install to run this application.
        please check out https://installpython3.com/" >&2
        exit 1
fi

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py 
deactivate