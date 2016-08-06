from datetime import datetime
from models import Photo
from models import session as db_session
from pytz import timezone

import settings
import random
import time
import vk

session = vk.Session(access_token=settings.VK['access_token'])
vkapi = vk.API(session, v=5.50)
time_zone = timezone(settings.TIME_ZONE)


class VkPhoto:
    def __init__(self, photo, album):
        self.photo = photo
        self.album = album

    def get_link(self):
        photo = self.photo
        link = photo[sorted(
                [x for x in photo.keys() if 'photo' in x],
                key=lambda x: int(x.split('_')[1])
            )[-1]]
        return link

    def get_caption(self):
        album = self.album
        photo = self.photo
        caption = "%s" % album['title']
        if photo['text']:
            caption = caption + "\n{}".format(photo['text'])
        date = datetime.fromtimestamp(
            photo['date'], tz=time_zone
        )
        caption = caption + "\n{:%d %b %Y}".format(date)
        return caption

    def save(self):
        link = self.get_link()
        photo = Photo(vk_id=self.photo['id'], link=link)
        db_session.add(photo)
        db_session.commit()


class VkPhotos:
    def __init__(self, owner_id):
        self.owner_id = owner_id

    def get_random_photo(self):
        albums = vkapi.photos.getAlbums(owner_id=self.owner_id).get('items')
        if not albums:
            return
        excluded_albums = settings.VK['excluded_albums']
        albums = [
            album for album in albums if album['id'] not in excluded_albums
        ]
        random.shuffle(albums)
        posted_photos = [
            vk_id[0] for vk_id in db_session.query(Photo.vk_id).distinct().all()
        ]
        while albums:
            album = albums.pop()
            photos = vkapi.photos.get(
                owner_id=self.owner_id, album_id=album['id'])['items']
            time.sleep(0.4)
            photos = [
                photo for photo in photos if photo['id'] not in posted_photos
            ]
            if photos:
                photo = random.choice(photos)
                vk_photo = VkPhoto(photo, album)
                return vk_photo
        return

    def get_count(self):
        count = vkapi.photos.getAll(owner_id=self.owner_id)['count']
        return count

    def posted_count(self):
        return db_session.query(Photo).count()
