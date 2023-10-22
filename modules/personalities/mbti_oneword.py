import random

from graia.amnesia.message import MessageChain
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.element import At, Plain
from graia.ariadne.message.parser.base import DetectPrefix
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.saya.channel import ChannelMeta

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "mbti一言"
channel.meta['description'] = "mbti一言"
channel.meta['author'] = "ltzXiaoYanMo"

words = open('./data/oneword.txt', encoding='utf-8').readlines()


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[DetectPrefix("!mbti_oneword")]
    )
)
async def mbti_oneword(app: Ariadne, event: GroupMessage, group: Group,
                       message: MessageChain = DetectPrefix("!mbti_oneword")):
    if str(message) != "":
        has_word = False
        for word in words:
            if word.strip()[-4:] == str(message).strip().upper():
                has_word = True
                await app.send_message(
                    group,
                    MessageChain([
                        At(event.sender),
                        Plain("\n"),
                        Plain(word.strip())
                    ])
                )
                break
        if not has_word:
            await app.send_message(
                group,
                MessageChain([
                    At(event.sender),
                    Plain("\n"),
                    Plain("找不到该MBTI类型！")
                ])
            )
    else:
        await app.send_message(
            group,
            MessageChain([
                At(event.sender),
                Plain("\n"),
                Plain(words[random.randrange(0, len(words))].strip())
            ])
        )
