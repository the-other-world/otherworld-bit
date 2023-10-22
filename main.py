# OtherWorldBit，异世界天体气象监测机器人

# Copyright(C) 2023 Abjust 版权所有。

# 本程序是自由软件：你可以根据自由软件基金会发布的GNU Affero通用公共许可证的条款，即许可证的第3版或（您选择的）任何后来的版本重新发布它和/或修改它。

# 本程序的发布是希望它能起到作用。但没有任何保证；甚至没有隐含的保证。本程序的分发是希望它是有用的，但没有任何保证，甚至没有隐含的适销对路或适合某一特定目的的保证。 参见 GNU Affero通用公共许可证了解更多细节。

# 您应该已经收到了一份GNU Affero通用公共许可证的副本。 如果没有，请参见<https://www.gnu.org/licenses/>。


import json
import os.path

from creart import create
from graia.ariadne.app import Ariadne
from graia.ariadne.connection.config import (
    HttpClientConfig,
    WebsocketClientConfig,
    config,
)
from graia.saya import Saya
from loguru import logger

import globalvars

# 初始化
verifykey = ""
if not os.path.exists("data.json"):
    obj = {
        "collected_at": 946656000,
        "high_temp_days": 0,
        "day_temp": 0.00,
        "day_hum": 0.00,
        "cycle_0": 946656000,
        "cycle_now": 946656000,
        "cycle_temp": 0.00
    }
    jobj = json.dumps(obj, indent=4)
    with open("data.json", "w") as outfile:
        outfile.write(jobj)
if not os.path.exists("config.txt"):
    lines = ["bot_qq=", "verify_key="]
    f = open("config.txt", "w")
    f.writelines(line + '\n' for line in lines)
    f.close()
    input("配置文件已创建！现在，你需要前往项目文件夹或者程序文件夹找到config.txt并按照要求编辑（按回车键退出）")
    exit(0)
else:
    f = open('config.txt')
    for line in f.readlines():
        split = line.split("=")
        if len(split) == 2:
            if split[0] == "bot_qq":
                globalvars.botqq = int(split[1].strip())
            elif split[0] == "verify_key":
                verifykey = split[1].strip()

# 启动机器人程序
saya = create(Saya)
app = Ariadne(
    connection=config(
        globalvars.botqq,  # 你的机器人的 qq 号
        verifykey,  # 填入你的 mirai-api-http 配置中的 verifyKey
        # 以下两行（不含注释）里的 host 参数的地址
        # 是你的 mirai-api-http 地址中的地址与端口
        # 他们默认为 "http://localhost:8080"
        # 如果你 mirai-api-http 的地址与端口也是 localhost:8080
        # 就可以删掉这两行，否则需要修改为 mirai-api-http 的地址与端口
        HttpClientConfig(host="http://localhost:8081"),
        WebsocketClientConfig(host="http://localhost:8081"),
    ),
)

# 加载模块
with saya.module_context():
    for root, dirs, files in os.walk("./modules", topdown=False):
        for name in files:
            module = os.path.join(root, name).replace('\\', '.').replace('./', '').replace('/', '.').split('.')
            if '__pycache__' in module:
                continue
            if module[1] == 'NO_USE':
                continue
            module = '.'.join(module)[:-3]
            logger.info(f'{module} 将被载入')
            saya.require(module)

for module, channel in saya.channels.items():
    logger.info(f"module: {module}")
    logger.info(f"name: {channel.meta['name']}")
    logger.info(f"author: {' '.join(channel.meta['author'])}")
    logger.info(f"description: {channel.meta['description']}")

logger.success('恭喜！启动成功，0Error，至少目前如此，也祝你以后如此')
app.launch_blocking()
