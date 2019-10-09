import time
import vk_api.longpoll
from vk_api.longpoll import VkEventType
# import Sources.GameMaster

token = "5cad23a9faf55f4af4ac7d41e2d4a8b7c5625d2a341eb01f084369ac250b8f106b9d7e7772790570073c9"
session = vk_api.vk_api.VkApi(token=token)

vk = session.get_api()
longpoll = vk_api.longpoll.VkLongPoll(session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.from_user and event.text:
        # result = GameMaster.sendMessage(event.text)
        vk.messages.send(user_id=event.user_id, message="heheboi %s" % time.time(), random_id=time.time())
