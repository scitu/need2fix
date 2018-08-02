#!/bin/bash

dir_name="env"

if [ -d $dir_name ]
then
    echo "Environment already exists"
else
    mkdir -p $dir_name
    virtualenv -p /usr/bin/python3 $dir_name

fi
source env/bin/activate
pip install -r need2fix/requirement.txt
