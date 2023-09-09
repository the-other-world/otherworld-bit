from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.saya.channel import ChannelMeta


channel = Channel[ChannelMeta].current()
channel.meta['name'] = "显示版本"
channel.meta['description'] = "显示OtherWorldBit的当前版本"
channel.meta['author'] = "Abjust"


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("版本")]
    )
)
async def display(app: Ariadne, group: Group):
    await app.send_message(
        group,
        "机器人版本：OtherWorldBit 1.0.2\n"
        "上次更新日期：2023/9/9\n"
        "更新内容：移除了Herobrine（？）"
    )
