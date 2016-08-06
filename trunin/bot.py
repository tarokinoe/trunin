from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
from vk_utils import VkPhotos
import re
import settings


updater = Updater(token=settings.TGMBOT['token'])
dispatcher = updater.dispatcher

vk_photos = VkPhotos(settings.VK['owner_id'])


def start(bot, update):
    bot.sendMessage(
        chat_id=update.message.chat_id,
        text="Здравствуйте, а вы кто собственно будете?"
    )

dispatcher.add_handler(CommandHandler('start', start))


def hello(bot, update):
    pattern = re.compile(
        r'.*(привет|здорово|здравствуйте|превед|здарова).*',
        flags=re.IGNORECASE
    )
    match = pattern.match(update.message.text)
    if match:
        bot.sendMessage(chat_id=update.message.chat_id, text='Привет!')

dispatcher.add_handler(MessageHandler([Filters.text], hello))


def images_count(bot, update):
    count = vk_photos.get_count()
    posted_count = vk_photos.posted_count()
    rest_count = count - posted_count
    text = "В группе {} фото, из них {} я уже послал, осталось {}".format(
        count, posted_count, rest_count
    )
    bot.sendMessage(
        chat_id=update.message.chat_id,
        text=text
    )

dispatcher.add_handler(CommandHandler('images_count', images_count))


def get_img(bot, update):
    vk_photo = vk_photos.get_random_photo()
    if not vk_photo:
        bot.sendMessage(chat_id=update.message.chat_id, text="Я не нашел фото")
        return
    link = vk_photo.get_link()
    caption = vk_photo.get_caption()
    try:
        bot.sendPhoto(
            chat_id=update.message.chat_id,
            photo=link,
            caption=caption
        )
    except:
        pass
    else:
        vk_photo.save()

dispatcher.add_handler(CommandHandler('get_img', get_img))
