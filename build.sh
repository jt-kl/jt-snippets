#!/bin/bash
# * Shell script to update package manifest and build a distribution wheel file

clear

source .env/bin/activate

pip3 install wheel --no-cache-dir
pip3 install -r requirements.txt --no-cache-dir
pip3 install redist/*
pip3 install -e .

python3 -m build
