import random

import requests
from graia.amnesia.message import MessageChain
from graia.ariadne.app import Ariadne
from graia.ariadne.event.mirai import NudgeEvent
from graia.ariadne.message.element import Plain, At
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.saya.channel import ChannelMeta

import globalvars

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "祖安"
channel.meta['description'] = "戳一戳祖安"
channel.meta['author'] = "Abjust"

api_list = [
    "https://api.qhsou.com/api/zuan.php",
    "http://api.qemao.com/api/yulu/?type=2"
]


@channel.use(ListenerSchema(listening_events=[NudgeEvent]))
async def nudge(app: Ariadne, event: NudgeEvent):
    # 只检测被戳的是不是机器人
    if event.target == globalvars.botqq:
        data = requests.get(random.choice(api_list),
                            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64))"})
        await app.send_group_message(
            event.subject,
            MessageChain([At(event.supplicant), Plain(f" {data.text.strip()}")])
        )
