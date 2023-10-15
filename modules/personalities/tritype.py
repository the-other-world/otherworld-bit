from textwrap import dedent

from graia.amnesia.message import MessageChain
from graia.ariadne import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import DetectPrefix
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema
from graia.saya.channel import ChannelMeta

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "Tritype"
channel.meta['description'] = "各九型人格Tritype类型解说"
channel.meta['author'] = "Abjust"

tritype_list = {}


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[DetectPrefix("!ttype")]
    )
)
async def tritype(app: Ariadne, group: Group, message: MessageChain = DetectPrefix("!ttype")):
    if str(message) != "":
        await app.send_message(
            group,
            dedent(
                tritype_list.get(
                    str(message).strip().lower(),
                    "找不到关于该九型人格类型的解释！"
                )
            )
        )
    else:
        await app.send_message(group, "输入!ttype <类型>可查看关于该九型人格的解释！")