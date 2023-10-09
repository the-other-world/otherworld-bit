from datetime import datetime, timezone
from textwrap import dedent

from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.saya.channel import ChannelMeta

import calc.temp
from calc import owct, temp

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "天体信息"
channel.meta['description'] = "看看异世界现在怎么样了"
channel.meta['author'] = "Abjust"


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("!info")]
    )
)
async def planet_info(app: Ariadne, group: Group):
    now = owct.get_time()
    utcnow = datetime.now(timezone.utc)
    now_temp = temp.get_temp()
    await app.send_message(group, dedent(f"""\
            OtherWorldBit
            异世界气象信息
            现在是：{utcnow.year + 1024}/{utcnow.month}/{utcnow.day} {now.hour}:{now.minute:02d}
            预警：{calc.temp.get_warn()}
            天气：undefined
            气温：{now_temp} ℃
            空气质量：undefined
            湿度：undefined %
            风：undefined风 undefined级
            气压：undefined hPa
            """))
