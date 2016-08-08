#!/bin/bash

USER_HOME=$(eval echo ~$USER)
source $USER_HOME/.virtualenvs/trunin/bin/activate
cd $USER_HOME/trunin/trunin
$USER_HOME/trunin/trunin/manage.py send_photo
deactivate
