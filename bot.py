import os
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from dotenv import load_dotenv


load_dotenv()
VK_TOKEN = os.getenv('TOKEN')
GROUP_ID = os.getenv('GROUP_ID')

def main():
    """ Пример использования bots longpoll
        https://vk.com/dev/bots_longpoll
    """

    vk_session = vk_api.VkApi(token=VK_TOKEN)

    longpoll = VkBotLongPoll(vk_session, GROUP_ID)
    vk = vk_session.get_api()
    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print('Новое сообщение:')

            print('Для меня от: ', end='')
            dt = event.obj.message['from_id']
            print(dt)

            print('Текст:', event.obj.message['text'])
            print()

            vk.messages.send(
                user_id=event.obj.message['from_id'],

                random_id=get_random_id(),
                message=("Новое сообщение - " + event.obj.message['text'])
            )
            print('ok')

        elif event.type == VkBotEventType.MESSAGE_REPLY:
            print('Новое сообщение:')

            print('От меня для: ', end='')

            print(event.obj.peer_id)

            print('Текст:', event.obj.text)
            print()

        elif event.type == VkBotEventType.MESSAGE_TYPING_STATE:
            print('Печатает ', end='')

            print(event.obj.from_id, end=' ')

            print('для ', end='')

            print(event.obj.to_id)
            print()

        elif event.type == VkBotEventType.GROUP_JOIN:
            print(event.obj.user_id, end=' ')

            print('Вступил в группу!')
            print()

        elif event.type == VkBotEventType.GROUP_LEAVE:
            print(event.obj.user_id, end=' ')

            print('Покинул группу!')
            print()

        else:
            print(event.type)
            print()


if __name__ == '__main__':
    main()
