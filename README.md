## About
This small application can post photo from [vkontakte](https://vk.com) to [telegram](https://telegram.org/) group chat
## Deployment
1. Create [vk application](https://new.vk.com/dev/standalone).

 Get vk token with this url https://oauth.vk.com/authorize?client_id=424242&display=page&scope=offline,photos&response_type=token&v=5.53 (change client_id value to your vk application id)

2. Create [telegram bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot)

3. Download this application
```
git clone https://github.com/tarokinoe/trunin.git trunin
cd trunin
```
4. Create virtualenv and install requirements
```
mkvirtualenv --python=/usr/bin/python3 trunin
workon trunin
pip install pip-tools
pip-sync requirements/base.txt
```
5. Create database:
```
cd trunin
./manage.py dbcreate
```
6. Create settings.json, replace values to yours
```
cp settings.json.example settings.json
```
```
{
    "tgmbot_token": "424242424242", // telegram bot token
    "tgmbot_group_chat_id": "42424242", // telegram group chat id
    "vk_access_token": "42424242442", //vk access token
    "vk_owner_id": "-424242", // vk owner of photos
    "vk_excluded_albums": [
        "42424242",
        "4242424242",
        "424242424242"
    ], // albums you want to exclude from posting
    "timezone": "Asia/Irkutsk"
}
```
7. Add cron job. In this example we have added job, which will run /path/to/trunin/trunin/send_photo.sh everyday at 12 o'clock.
```
sudo crontab -u trunin -e
```
```
0 12 * * * /home/trunin/trunin/trunin/send_photo.sh
```
