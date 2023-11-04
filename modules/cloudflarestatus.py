from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
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
channel.meta['author'] = "ltzXiaoYanMo"

web =


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("!cfstatus")]
    )
)
async def status(app: Ariadne, group: Group):
    await app.send_message(
        group,
        requests.get(json.loads(requests.get(CloudStatus).text)['components'][0]['name']).text
    )
