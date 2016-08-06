from vk_utils import VkPhotos
import settings
import telegram


vk_photos = VkPhotos(settings.VK['owner_id'])
bot = telegram.Bot(token=settings.TGMBOT['token'])


def send_photo():
    vk_photo = vk_photos.get_random_photo()

    if not vk_photo:
        return

    link = vk_photo.get_link()
    caption = vk_photo.get_caption()

    try:
        bot.sendPhoto(
            chat_id=settings.TGMBOT['group_chat_id'],
            photo=link,
            caption=caption
        )
    except:
        pass
    else:
        vk_photo.save()
