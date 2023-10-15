from textwrap import dedent

from graia.amnesia.message import MessageChain
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import DetectPrefix
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.saya.channel import ChannelMeta

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "MBTI"
channel.meta['description'] = "各MBTI类型解说"
channel.meta['author'] = "Abjust, ltzXiaoYanMo"

mbti_list = {
    # INTP简介
    "intp": """\
    只有 3% 的人口为逻辑学家型人格，极为罕见，尽管如此，他们也并不以为意，因为他们根本不屑与“平庸”为伍。 
    逻辑学家们展现出积极主动的创造性，异于常人的视角以及永不枯竭的智慧，这都令他们深感自豪。
    人们常常将逻辑学家称为哲学家、思考者，或是爱空想的教授，在历史的长河中，许多科学发现就是他们的智慧之花结出的丰硕果实。
    数据来源于 https://www.16personalities.com/ch/intp-%E4%BA%BA%E6%A0%BC
    """,
    # INTJ简介
    "intj": """\
    人们常说，高处不胜寒。作为人数最少且战略能力最强的人格类型之一，“建筑师”们对此深有体会。 
    他们仅占人口的 2%，女性则更为稀少，只有 0.8%。这让他们很难找到志同道合能够与其过人的智慧和审慎的思考方式比肩的同类。 
    建筑师人格类型的人想象力丰富却很果断，雄心壮志但注重隐私，充满好奇心但从不浪费精力。
    数据来源于 https://www.16personalities.com/ch/intj-%E4%BA%BA%E6%A0%BC
    """,
    # ENTP简介
    "entp": """\
    辩论家人格类型的人是故意持相反意见的人，善于把观点和信条剪得支离破碎并撒在空中给所有人看。  
    与更有决心的人格类型相比，“辩论家”这样做并非想要取得更深层的含义或战略性的目标，而仅仅因为有趣。 
    没人比“辩论家”们更喜欢头脑的交锋，因为这可以给他们一个运用聪明才智，连结不同想法来证明自己观点的机会。
    数据来源于 https://www.16personalities.com/ch/entp-%E4%BA%BA%E6%A0%BC
    """,
    # ENTJ简介
    "entj": """\
    指挥官人格类型的人是天生的领导者。 这种人格类型的人天生具有魅力和信心，他们所散发的权威性能召集大家为着一个共同目标努力。 
    但与领导者人格类型有所不同的是，他们的性格中有着近乎残酷的理性，用强大的动力、坚定的决心和锋芒毕露的思想实现为自己制定的一切目标。
    好在只有 3% 的人口具有这种人格类型，否则就会无情碾压那些剩下的大多数胆小又敏感的人格类型。
    但是对于许多我们习以为常的公司和机构，我们都要感谢他们的贡献。
    数据来源于 https://www.16personalities.com/ch/entj-%E4%BA%BA%E6%A0%BC
    """,
    # INFP简介
    "infp": """\
    调停者人格类型的人是真正的理想主义者，他们总是从最坏的人和事中寻找最好的一面，想方设法让情况变得更好。 
    虽然可能看起来冷静，内向甚至害羞，但他们内心的火焰和热情可以光芒四射。 
    他们仅占人口的4%，常常被人误解，但当他们找到志同道合的人时，他们之间的和谐就像是快乐和灵感的源泉。 
    数据来源于 https://www.16personalities.com/ch/infp-%E4%BA%BA%E6%A0%BC
    """,
    # INFJ简介
    "infj": """\
    提倡者人格类型的人非常稀少，只有不到 1% 的人口属于这种类型，但他们对世界的贡献不容忽视。 
    他们具有与生俱来的理想主义和道德感，但真正令他们与其他理想主义人格类型区分开来的是，他们果断决绝。
    他们不是懒散的空想家，而是能脚踏实地完成目标，留下深远的积极影响的人。
    数据来源于 https://www.16personalities.com/ch/infj-%E4%BA%BA%E6%A0%BC
    """,
    # ENFP简介
    "enfp": """\
    竞选者人格类型的人是真正富有自由精神的人。
    他们常常是聚会上的焦点，但是与眼前的兴奋和快乐相比，他们更享受与人们建立的社会和情感联系。 
    富有魅力，独立，精力充沛且有同情心，占人口 7% 的他们在人群中随处可见。
    数据来源于 https://www.16personalities.com/ch/enfp-%E4%BA%BA%E6%A0%BC
    """,
    # ENFJ简介
    "enfj": """\
    主人公人格类型的人是天生的领导者，充满激情，魅力四射。 
    这类型人格的人约占人口的 2%，他们常常是我们的政客，教练和老师，帮助、启发他人取得成就并造福整个世界。 
    他们浑身散发着天然的自信，潜移默化地影响着周围的人，也能够指导他人团结协作，帮助他们提升自己并改进社区，而他们自己也可从中获得自豪感与快乐。
    数据来源于 https://www.16personalities.com/ch/enfj-%E4%BA%BA%E6%A0%BC
    """,
    # ISFJ简介
    "isfj": """\
    守卫者人格类型是一个很独特的类型，他们的许多品质都与他们自身的特质不相符。 
    虽然非常照顾他人的感受，一旦到了需要保护其家人或朋友的时候，会变得非常强悍；
    虽然安静内向，却有很好的社交技巧和强大的社会关系；虽然追求安全和稳定，但只要他们得到了理解和尊重，就愿意接受改变。
    和很多事物一样，具有守卫者人格类型的人作为一个整体不可小觑，他们的身份由他们如何使用这些强项而定义。
    数据来源于 https://www.16personalities.com/ch/isfj-%E4%BA%BA%E6%A0%BC
    """,
    # ISTJ简介
    "istj": """\
    军需官人格类型的人被认为是数量最多的，大约占人口总数的 13%。 
    他们有很多明显的特征，例如正直，务实，恪尽职守，使他们深受家庭以及拥护传统，规则，标准的组织的青睐，比如律所，监管部门和军队。
    这种人格类型的人愿意为自己的行为负责，为努力完成目标所做的一切感到骄傲。他们会毫不吝啬时间和精力，耐心准确地完成每个任务。
    数据来源于 https://www.16personalities.com/ch/istj-%E4%BA%BA%E6%A0%BC
    """,
    # ESFJ简介
    "esfj": """\
    最适合形容“执政官”们的词就是“受欢迎”了 — 这也符合常理，因为他们大约占人口的 12%，是非常常见的类型。 
    在中学里，他们常常是拉拉队员或四分卫，在聚光灯下带领着队伍走向胜利和荣誉。 
    在以后的人生里，“执政官”同样享受去支持他们的朋友和爱着的人，组织聚会，尽一切可能让每个人开心。
    数据来源于 https://www.16personalities.com/ch/esfj-%E4%BA%BA%E6%A0%BC
    """,
    # ESTJ简介
    "estj": """\
    执行官人格类型的人是传统和秩序的代表，利用他们对正确，错误，和社会标准的理解来团结家庭和社区。 
    他们诚实，爱奉献，有尊严，他们的明确建议和指导被人看重，也愿意披荆斩棘，带领大家努力前行。 
    他们会因为团结大家而骄傲，常常承担起社区组织者的角色，努力组织大家一起庆祝当地重要的节日，或守护着那些使家庭和社区紧密相连的传统价值观。
    数据来源于 https://www.16personalities.com/ch/estj-%E4%BA%BA%E6%A0%BC
    """,
    # ISFP简介
    "isfp": """\
    探险家人格类型的人是真正的艺术家，这并不是说他们是通常意义上的兴高采烈到郊外画几棵小树的画家。
    但他们通常都精于此道。 他们会运用审美，设计，甚至选择和行动来打破社会常规。 
    探险家人格类型的人喜欢用美感和行为方面的实验来颠覆传统的期望。很有可能他们已经说过不止一次“不要控制我！”
    数据来源于 https://www.16personalities.com/ch/isfp-%E4%BA%BA%E6%A0%BC
    """,
    # ISTP简介
    "istp": """\
    艺术能手人格类型的人喜欢用双手和眼睛去探索事物，他们通过冷静的理性主义和精神饱满的好奇心来感知和体验这个世界。
    拥有这种人格的人是天生的制造者，他们在不同的项目中穿梭，从创造有用、充足的产物中获得乐趣，并在创造的过程中从外界学习。
    艺术能手人格类型的人通常是机械师和工程师，他们亲手拆卸东西，并把它们安装还原到比之前更好一点的状态，从中获得极大的乐趣。
    数据来源于 https://www.16personalities.com/ch/istp-%E4%BA%BA%E6%A0%BC
    """,
    # ESFP简介
    "esfp": """\
    如果有人总是不由自主地开始又唱又跳，可以将其划分为表演者人格类型。
    表演者人格类型的人会沉醉于当前的兴奋状态，而且希望人人如此。 
    说起激励他人，给他人打气助威，表演者人格类型的人会毫不吝惜自己的时间和精力，令人难以招架，任何其他人格类型在这方面都不能与之相提并论。
    数据来源于 https://www.16personalities.com/ch/esfp-%E4%BA%BA%E6%A0%BC
    """,
    # ESTP简介
    "estp": """\
    企业家人格类型的人对周围的环境颇有影响 — 在聚会上发现他们的最好方式就是去找那些在人群中穿梭自如的人。
    他们带着直接而朴实的幽默谈笑风生，喜欢成为人群中的焦点。
    如果观众被邀请上台，他们会自荐，或推荐一个害羞的朋友。
    数据来源于 https://www.16personalities.com/ch/estp-%E4%BA%BA%E6%A0%BC
    """
}


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[DetectPrefix("!mbti")]
    )
)
async def mbti(app: Ariadne, group: Group, message: MessageChain = DetectPrefix("!mbti")):
    if "_oneword" not in str(message):
        if str(message) != "":
            await app.send_message(
                group,
                dedent(
                    mbti_list.get(
                        str(message).strip().lower(),
                        "找不到关于该 MBTI 类型的解释！请检查您的输入是否有误"
                    )
                )
            )
        else:
            await app.send_message(group, "输入!mbti <类型:字符串>可查看关于该MBTI类型的解释！")
