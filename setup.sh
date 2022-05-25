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

