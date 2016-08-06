import json


with open("settings.json") as f:
    settings = json.loads(f.read())


def get_setting(setting, settings=settings):
    """Get the secret variable or return explicit exception."""
    try:
        return settings[setting]
    except KeyError:
        error_msg = "Set the {0} variable".format(setting)
        raise KeyError(error_msg)

# Trunin bot
TGMBOT = {
    "token": get_setting('tgmbot_token'),
    "group_chat_id": get_setting('tgmbot_group_chat_id')
}


# VK
VK = {
    'access_token': get_setting('vk_access_token'),
    'owner_id':  get_setting('vk_owner_id'),
    'excluded_albums': get_setting('vk_excluded_albums')
}

TIME_ZONE = get_setting('timezone')
