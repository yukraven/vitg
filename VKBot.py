import logging.config
import time
import vk_api.longpoll
from vk_api.longpoll import VkEventType
import Sources.GameMaster

logging.config.fileConfig("Logs/logging.conf")
log = logging.getLogger("vkbot")

token = "5cad23a9faf55f4af4ac7d41e2d4a8b7c5625d2a341eb01f084369ac250b8f106b9d7e7772790570073c9"
log.info("создание сессии")
session = vk_api.vk_api.VkApi(token=token)
log.info("получение апи")
vk = session.get_api()
log.info("создание лонгполла")
longpoll = vk_api.longpoll.VkLongPoll(session)

log.info("создание гейм-мастера")
GM = Sources.GameMaster.GameMaster()

log.info("начинаем слушать лонгполл")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.from_user and event.text:
        log.info("от пользователя с id '%s' получили сообщение - '%s'" % (event.user_id, event.text))
        try:
            log.info("отдаем гейм-мастеру")
            result = GM.sendMessage(event.text, event.user_id)
            log.info("получаем ответ '%s' и отправляем пользователю" % result)
            vk.messages.send(user_id=event.user_id, message=result, random_id=time.time())
        except Exception as e:
            log.error(e)
            vk.messages.send(user_id=event.user_id, message="Непредвиденная ошибка", random_id=time.time())
