#!/bin/bash

SCRIPT_DIR="$(pwd)"
source /usr/local/bin/virtualenvwrapper.sh
workon trunin
cd $SCRIPT_DIR
./manage.py send_photo
deactivate