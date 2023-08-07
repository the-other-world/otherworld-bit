from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema


channel = Channel.current()
channel.name("天体信息")
channel.description("看看异世界现在怎么样了")
channel.author("Abjust")


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage]
    )
)
async def display(app: Ariadne, group: Group, message: MessageChain):
    if message.display == "!info":
        await app.send_message(group, "机器人版本：OtherWorldBit 1.0.0\n上次更新日期：2023/8/7\n更新内容：OtherWorldBit 初始版本")
