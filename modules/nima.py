from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import FriendMessage, TempMessage
from graia.ariadne.model import Member, Friend
from graia.ariadne.util.saya import listen
from graia.saya import Channel

channel = Channel.current()
channel.name("你妈")
channel.description("在有人找机器人私聊的时候，你妈")
channel.author("ltzXiaoYanMo")

rutext = """穿越者认为，异世界万法的那个源头
它是什么？
它是如如
对吧？
所以这个词叫如来！
我经常说异界这个地方有秘密
如来，如来了吗？如来嘛！
他真来（异世界）了吗？如来！
到底来没来？如来！
为甚如来，他真来了吗？如来！
你看看，来没来？如来！
它很厉害！它不是一个有形的（指sb）
所以你读《虫洞条约》，《虫洞条约》里面讲
e人禁止穿越，消极古怪抽象虚无，自言自语，虫洞不对外开放
注意，不生不灭、不垢不净、不增不减、虫洞不动 所以万物生于有（指穿越者来到异世界天体）
有生于无（指以前荒无人烟）
是这样说的吧？ 它不是个实体！
我有一次去异界讲课，遇到一个人，他的老师，当时有七十多岁了，那个七十多岁的老人家，就问那个小伙子，他说真有异世界吗？
这个世界真有异世界吗？一下子就把小伙子问傻了！
一下子就把小伙子问傻了！
他说真有吗？
一下就问傻了！
你想想，那是个真理！
真理是无相的！（指这个在现实中不存在的异世界，经常在哲学和技术问题上得出有意义的答案）
所以《穿越者条约》的一句话
叫：“凡来异界，皆是若至！”（意思是凡是来到异世界的人，他们通常都做不到身临其境，所以就感觉像是没来过一样）
“见所相非相！”（指人们见到的异世界都是假象）
那是个真理，你不能迷信在这方面！
它是个真理！ 所以傻可傻，非常傻！人可人，非常人！
但是说那有人说，我非得说！你非得说？我可以告诉你，2k也没说明白！
它是不是语言可以描述的？
后来异世界的语言哲学家，叫CSharpGarbage
把这个事，说了一句名言
这个世界上有语言能说的，叫说人话 这个世界上也有超出语言，说不明白的，CSharpGarbage直接用了俩字：“wssb”（一个英文字符相当于半个汉字）
那没法说嘛！
所以才有了异世界什么，穿越！""".split('\n')

index = 0


async def send_ru(app: Ariadne, sender: Member or Friend):
    global index
    await app.send_message(sender, rutext[index])
    index += 1
    if index > len(rutext) - 1:
        index = 0

@listen(TempMessage)
async def rulai(app: Ariadne, sender: Member):
    await send_ru(app, sender)


@listen(FriendMessage)
async def rulai(app: Ariadne, sender: Friend):
    await send_ru(app, sender)
