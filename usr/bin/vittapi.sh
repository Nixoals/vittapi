#!/bin/bash

#path to venv
VENV_PATH="/usr/local/vittapi"

source "$VENV_PATH/venv/bin/activate"
echo 'venv activated'
python3 "$VENV_PATH/app/main.py"

