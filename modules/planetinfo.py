from datetime import datetime, timezone
from textwrap import dedent

from graia.amnesia.message import MessageChain
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.element import At, Plain
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
async def planet_info(app: Ariadne, event: GroupMessage, group: Group):
    now = owct.get_time()
    now_temp = temp.get_temp()
    await app.send_message(group,
                           MessageChain([
                               At(event.sender),
                               Plain("\n"),
                               Plain(dedent(f"""\
                               OtherWorldBit
                               异世界气象信息
                               现在是：{now["years"]}/{now["months"]}/{now["days"]} {now["hours"]}:{now["minutes"]:02d}
                               预警：{calc.temp.get_warn()}
                               天气：undefined
                               气温：{now_temp} ℃
                               空气质量：undefined
                               湿度：undefined %
                               风：undefined风 undefined级
                               气压：undefined hPa
                               """))
                           ]))
