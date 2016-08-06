## Deployment
Create virtualenv
```
mkvirtualenv --python=/usr/bin/python3 trunin
pip install pip-tools
pip-sync requirements/base.txt
```
Create database:
```
cd trunin
./manage.py dbcreate
```
cron
```
/path/to/virtualenv/trunin/send_photo.sh
```
