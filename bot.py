import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from dotenv import load_dotenv
from db_get import select_products, select_categories

load_dotenv()
VK_TOKEN = os.getenv('TOKEN')
GROUP_ID = os.getenv('GROUP_ID')
KEY = os.getenv('KEY')
TS = os.getenv('TS')
PTS = os.getenv('PTS')
SERVER = os.getenv('SERVER')


def generate_menu(items):
    keyboard = VkKeyboard(one_time=True)
    for i in range(len(items)-1):
        keyboard.add_button(items[i], color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
    keyboard.add_button(items[len(items)-1], color=VkKeyboardColor.NEGATIVE)


def main():
    """ Главная логика бота
    """
    vk_session = vk_api.VkApi(token=VK_TOKEN)
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    items = select_categories()
    keyboard = VkKeyboard(one_time=True)
    for i in range(len(items)-1):
            keyboard.add_button(items[i], color=VkKeyboardColor.NEGATIVE)
            keyboard.add_line()
    keyboard.add_button(items[len(items)-1], color=VkKeyboardColor.NEGATIVE)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            text = event.text
            low_text = text.lower()
            vars1 = ['привет', 'ку', 'хай', 'хеллоу', 'hi']
            if low_text in vars1:
                if event.from_user:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Для начала работы напишите start',
                        random_id=get_random_id()
                        )
            vars2 = ['старт', 'start']
            if event.text in vars2:
                if event.from_user:
                    vk.messages.send(
                        user_id=event.user_id,
                        random_id=get_random_id(),
                        keyboard=keyboard.get_keyboard(),
                        message='Выберите категорию товара'
                        )
            if text in items:
                products = select_products(text)
                keyboard = VkKeyboard(one_time=True)
                for i in range(len(products)-1):
                    keyboard.add_button(products[i], color=VkKeyboardColor.POSITIVE)
                    keyboard.add_line()
                keyboard.add_button(items[len(products)-1], color=VkKeyboardColor.POSITIVE)
                if event.from_user:
                    vk.messages.send(
                        user_id=event.user_id,
                        random_id=get_random_id(),
                        keyboard=keyboard.get_keyboard(),
                        message='Выберите товар из представленных ниже'
                        )

if __name__ == '__main__':
    main()
