import os
from vk_api import VkApi
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('TOKEN')
PEER_ID = '-215636611'


def upload_photo(upload, photo):
    response = upload.photo_messages(photo)[0]

    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']

    return owner_id, photo_id, access_key


def send_photo(vk, peer_id, owner_id, photo_id, access_key):
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.messages.send(
        random_id=get_random_id(),
        peer_id=peer_id,
        attachment=attachment
    )


def main():
    vk_session = VkApi(token=TOKEN)
    vk = vk_session.get_api()
    upload = VkUpload(vk)

    send_photo(vk, PEER_ID, *upload_photo(upload, 'tort1.jpg'))


if __name__ == '__main__':
    main()