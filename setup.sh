#!/bin/sh

curl -o ./download.pkg "https://www.python.org/ftp/python/3.10.4/python-3.10.4-macos11.pkg"
open download.pkg
pip install virtualenv
git clone 'https://github.com/manu-yaff/Tesina'
cd Tesina
git checkout visualization-tool
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd vis_tool
python manage.py migrate
python manage.py runserver
$SHELL

