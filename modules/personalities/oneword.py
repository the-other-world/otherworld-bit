from graia.amnesia.message import MessageChain
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import DetectPrefix
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.saya.channel import ChannelMeta

import random

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "mbti一言"
channel.meta['description'] = "mbti一言"
channel.meta['author'] = "ltzXiaoYanMo"


words = open('./data/oneword.txt', encoding='utf-8').readlines()


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[DetectPrefix("!oneword")]
    )
)
async def mbti_oneword(app: Ariadne, group: Group, message: MessageChain = DetectPrefix("!oneword")):
    if str(message) != "":
        for word in words:
            if word[-5:].strip() == str(message).strip().upper():
                await app.send_message(
                    group,
                    word
                )
                break
    else:
        await app.send_message(
            group,
            words[random.randrange(0, len(words))]
        )
