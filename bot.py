import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})

token = 'vk1.a.ZXv581Qmb2N5vBK0XGM022HBZhjnV5ieXl5L3GZv4Wp9oqdNuj1cajG5wWA_n7bQ2fReBWjB0CLFiE7x3c202NCo1Yda7zFLdlEf0QtNSBRpUr_1won8B3q2w_-QMDcHKd1iwk2S8df1fKLu-y6Fpq6Bk-2W1ls8-XPMkRKajlwzqWenNM_QLI35T5No12aw'
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
        
            # Сообщение от пользователя
            request = event.text
            
            # Каменная логика ответа
            if request == "привет":
                write_msg(event.user_id, "Хай")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")