import json

import requests
from graia.amnesia.message import MessageChain
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import DetectPrefix
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.saya.channel import ChannelMeta

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "Go趋势"
channel.meta['description'] = "Golang模块下载量排行榜"
channel.meta['author'] = "Abjust"


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[DetectPrefix("!gotrend")]
    )
)
async def display(app: Ariadne, group: Group, message: MessageChain = DetectPrefix("!gotrend")):
    url = "https://goproxy.cn/stats/trends/latest"
    response = requests.get(url)
    if response.status_code == 200:
        contents = response.text
        json_dict = json.loads(contents)
        message_content = "Golang模块排行榜"
        skips = 0
        if str(message) != "":
            try:
                skips = int(str(message).strip()) - 1
                if skips < 0:
                    skips = 0
                    await app.send_message(group, "页码无效！（将默认为第一页）")
                elif skips > 99:
                    skips = 99
                    await app.send_message(group, "页码无效！（将默认为最后一页）")
            except TypeError:
                await app.send_message(group, "页码无效！（将默认为第一页）")
            except ValueError:
                await app.send_message(group, "页码无效！（将默认为第一页）")
        for i in range(10):
            message_content += (f"\n第 {i + skips * 10 + 1} 名"
                                f"\n模块路径：{json_dict[i + skips * 10].get('module_path')}"
                                f"\n下载次数：{json_dict[i + skips * 10].get('download_count')}")
        await app.send_message(group, message_content)
    else:
        await app.send_message(group, "拉取API失败！")
