#!/bin/sh
sudo python2 -m pip install virtualenv
virtualenv .
source bin/activate
pip2 install pygame
python2 main.py