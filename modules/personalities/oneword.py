from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.saya.channel import ChannelMeta

import requests
import ramdom

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "mbti一言"
channel.meta['description'] = "mbti一言"
channel.meta['author'] = "ltzXiaoYanMo"

text = './data/oneword.txt'

data = random.choice(open(text, encoding='utf-8').readlines()).strip()

@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("MBTI一言")]
    )
)
async def mbti_oneword(app: Ariadne, group: Group):
    await app.send_message(
        group,
        data
    )
