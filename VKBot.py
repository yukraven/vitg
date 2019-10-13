# coding: utf8
import logging.config
import time
import vk_api.longpoll
from vk_api.longpoll import VkEventType
import Sources.GameMaster

logging.config.fileConfig("Logs/logging.conf")
log = logging.getLogger("vkbot")


def getSession():
    while (True):
        try:
            log.info(u"открытие файла")
            file = open("token.conf", "r")
            log.info(u"получение токена")
            token = file.read()
            log.info(u"создание сессии")
            return vk_api.vk_api.VkApi(token=token)
        except Exception as exc:
            log.critical(u"не удалось получить сессию: %s" % exc)
            time.sleep(10)


session = getSession()
log.info(u"получение апи")
vk = session.get_api()
log.info(u"создание лонгполла")
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
