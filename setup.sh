#!/bin/sh

sudo apt-get install git -y
sudo apt-get install python3.9 -y
sudo apt-get install python3-pip -y
sudo apt-get install python3-venv -y
sudo apt-get install ffmpeg -y
cd Tesina
python3 -m venv .venv
source .venv/bin/activate
git checkout visualization-tool
pip3 install -r requirements.txt
cd vis_tool
./manage.py migrate
./manage.py runserver

# instalar git
# instalar python
# instalar pip
# instalar virtualenv
# requirements
# ffmpeg

# curl -o ./download.pkg "https://www.python.org/ftp/python/3.10.4/python-3.10.4-macos11.pkg"
# open download.pkg
# pip install virtualenv
# git clone 'https://github.com/manu-yaff/Tesina'
# cd Tesina
# git checkout visualization-tool
# python -m venv .venv
# source .venv/bin/activate
# pip install -r requirements.txt
# cd vis_tool
# python manage.py migrate
# python manage.py runserver
# $SHELL

