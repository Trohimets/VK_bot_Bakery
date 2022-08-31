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


def first_menu(items):
    keyboard = VkKeyboard(one_time=True)
    for i in len(items):
        for j in 1:
            button = items[i][0]
            keyboard.add_button('Торты', color=VkKeyboardColor.NEGATIVE)
            keyboard.add_button('Хлеб', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Выпечка', color=VkKeyboardColor.SECONDARY)


def main():
    """ Главная логика бота
    """

    vk_session = vk_api.VkApi(token=VK_TOKEN)

    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()

    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Торты', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button('Хлеб', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Выпечка', color=VkKeyboardColor.SECONDARY)
    # keyboard.add_line()
    # keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=215636611")

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            vars1 = ['Привет', 'Ку', 'Хай', 'Хеллоу', 'Hi', 'hi']
            if event.text in vars1:
                if event.from_user:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Привет) Для начала работы напиши start',
                        random_id=get_random_id()
                        )
            vars2 = ['старт', 'start']
            if event.text in vars2:
                if event.from_user:
                    vk.messages.send(
                        user_id=event.user_id,
                        random_id=get_random_id(),
                        keyboard=keyboard.get_keyboard(),
                        message='Держи'
                        )


if __name__ == '__main__':
    main()
