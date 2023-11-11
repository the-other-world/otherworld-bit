from graia.amnesia.message import MessageChain
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.element import At, Plain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.saya.channel import ChannelMeta

import requests
import json

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "CloudFlare状态检测"
channel.meta['description'] = "CloudFlare Status Checker"
channel.meta['author'] = "Abjust, ltzXiaoYanMo"

api = "https://www.cloudflarestatus.com/api/v2/status.json"


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("!cfstatus")]
    )
)
async def cloudflare_status(app: Ariadne, event: GroupMessage, group: Group):
    await app.send_message(
        group,
        MessageChain([
            At(event.sender),
            Plain("\n"),
            Plain(json.loads(requests.get(api).text)['status']['description'])
        ])
    )
