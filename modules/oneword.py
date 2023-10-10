from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import DetectPrefix
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema
from graia.saya.channel import ChannelMeta

import requests

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "OneWord"
channel.meta['description'] = "网易云一言（雾）"
channel.meta['author'] = "ltzXiaoYanMo"

# 获取api
hitokoto = "https://v1.hitokoto.cn/?encode=json"

# 收到API，获取一言
data = requests.get(hitokoto)

@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[DetectPrefix("YB一言")]
    )
)
async def oneword(app: Ariadne, group: Group):
    await app.send_message(
        group,
        hitokoto
    )