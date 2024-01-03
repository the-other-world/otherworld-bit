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

from calc import owct, weather

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
    now_weather = weather.get_weather()
    await app.send_message(group,
                           MessageChain([
                               At(event.sender),
                               Plain("\n"),
                               Plain(dedent(f"""\
                               OtherWorldBit
                               异世界气象信息
                               现在是：{now["years"]}/{now["months"]}/{now["days"]} {now["hours"]}:{now["minutes"]:02d}
                               预警：{now_weather["warnings"]}
                               天气：{now_weather["weather"]}
                               降水概率：{round(now_weather["preci_chance"] * 100)} %
                               降水量：{now_weather["precipitation"]} mm
                               气温：{now_weather["temp"]} ℃
                               湿度：{round(now_weather["hum"] * 100)} %
                               风：{now_weather["wind_direction"]}风
                               {now_weather["wind_scale"]}级（{now_weather["wind_speed"]} m/s）
                               气压：undefined hPa
                               """))
                           ]))
