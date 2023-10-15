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
channel.meta['name'] = "九型人格"
channel.meta['description'] = "各九型人格类型解说"
channel.meta['author'] = "Abjust"


enneagram_list = {
    # 1w9简介
    "1w9": """\
    第一型人被称为“改革者”，因为他们总是在寻找改善世界、发挥影响力、施加压力和影响变革的方法。
    第九型人被称为“和平缔造者”，因为他们天生渴望解决冲突并创造和谐。
    九号侧翼将这些品质添加到了第一型人格中。
    这意味着 1w9 型人会渴望带来社会变革，但行为上会更加内向，较少对抗。
    这使得 1w9 型人变得彬彬有礼、矜持，但对他人和周围的世界也非常挑剔和评判。
    因此，九型人格 1w9 类型被称为“理想主义者”。 
    然而，与“改革者”不同的是，如果九号翼型人需要更加明显的外向性，他们可能会很难坚持自己的原则，这可能会导致他们显得冷漠或缺乏人情味。
    如果他们受到挑战或批评，因为 1w9 会试图避免冲突，这对他们来说也会很困难。
    这可能意味着“理想主义者”难以容忍消极情绪，有时可能会因为世界没有达到他们的高标准而感到沮丧。
    节选并翻译自 https://www.personalitydata.org/enneagram/type-1w9
    （注：如翻译质量不佳，请及时反映）
    """,
    # 1w2简介
    "1w2": """\
    第一型人被称为“改革者”，因为他们总是在寻找改善世界、发挥影响力、施加压力和影响变革的方法。
    第二型人被称为“助人者”，因为他们天生渴望帮助他人并以同理心行事。
    二号侧翼人格将这些品质添加到了第一型人格中。
    这意味着 1w2 型人渴望带来社会变革，但对其行为具有一定的人际敏感性。
    这可以使九型人格 1w2 在倡导有意义的社会变革时非常强大。
    因此，1w2 型被称为“倡导者”。 
    然而，与“改革者”不同的是，如果有可能给他人带来不便或不安，双翼型人可能会很难坚持自己的原则。
    如果他们的个人原则与他们的同理心相冲突，这对他们来说可能会很困难。
    这可能意味着“倡导者”因道德困境而难以通过内部冲突采取果断行动。
    节选并翻译自 https://www.personalitydata.org/enneagram/type-1w2
    （注：如翻译质量不佳，请及时反映）
    """,
    # 2w1简介
    "2w1": """\
    第二型人被称为“助人者”，因为他们总是寻找帮助他人、支持和保护他人的方法，以同理心和关怀的态度行事，以创造和谐并避免冲突。
    第一型人被称为“改革者”，因为他们有天生的动力去代表正义事业和原则来影响积极的改变。
    一号侧翼将这些品质添加到第二型人格中。
    这意味着 2w1 型人会渴望帮助、关心和保护他人，同时帮助更广泛的积极变革事业。
    这使得 2w1 型非常适合作为此类原因的伴侣。因此，2w1 型被称为“同伴”。 
    然而，与“帮助者”不同的是，当时代变得艰难和不和谐时，一翼可能会挣扎并变得没有安全感。
    在这些时刻，他们会寻求他人的赞扬来安抚自己，并且当他们试图安抚他人的需求时，可能会失去自己的个人需求。
    这可能意味着“同伴”很难在困难的情况下提供最有用的建议，而不是其他人可能想听到的建议。
    节选并翻译自 https://www.personalitydata.org/enneagram/type-2w1
    （注：如翻译质量不佳，请及时反映）
    """,
    # 2w3简介
    "2w3": """\
    第二型人被称为“助人者”，因为他们总是寻找帮助他人、支持和保护他人的方法，以同理心和关怀的态度行事，以创造和谐并避免冲突。
    第三型人被称为“成就者”，因为他们对进步和成就有着永不满足的动力，以及与生俱来的勤奋意识。
    三号侧翼将这些品质添加到了第二型人格中。
    这意味着 2w3 型人会渴望帮助、关心和保护他人，但也会有动力让他们在自己的领域表现出色。
    例如，2w3 将成为优秀的医生，因为他们既有同理心和情商，可以提供有效的护理，同时也有在其职业中取得成就所需的动力。
    同样，他们的超凡魅力行为倾向，加上他们对群体的关心，使他们成为出色的主人——关心他人的需求，同时提供大胆、前瞻性的控制感或领导力。
    因此，类型 2w3 被称为“东道主”。
    然而，与“帮助者”不同的是，三号翼型人可能会挣扎并变得不安全，因为他们不断需要被视为不仅有爱心和乐于助人，而且有能力和追求成就。
    这种无休止地寻求他人的赞扬和认可会让核心的第二型人变得更加困难，使他们变得非常专横，在最坏的情况下也让人讨人喜欢。
    节选并翻译自 https://www.personalitydata.org/enneagram/type-2w3
    （注：如翻译质量不佳，请及时反映）
    """,
    # 3w2简介
    "3w2": """\
    第三型人被称为“成就者”，因为他们总是在寻找实现的方法，完成目标，努力实现这些目标，并让别人知道他们的成就。
    第二型人被称为“助人者”，因为他们总是寻找帮助他人、支持和保护他人的方法，以同理心和关怀的态度行事，以创造和谐并避免冲突。
    二号侧翼人格为第三型人格增添了这些品质。
    这意味着 3w2 型人的目标是以竞争性和精力充沛的方式取得成就，但主要关注于获得他人的接受。
    这意味着他们最大的愿望是值得别人的爱，而他们最大的恐惧是得不到别人的爱。
    这可以使 3w2 型个体变得强大，但也带来麻烦。因此，3w2 型被称为“魅力者”。 
    然而，与“成就者”不同的是，两翼型人可能会挣扎并拼命地试图让别人喜欢他们。
    在这些时刻，他们会寻求他人的赞扬来安抚自己，并且当他们试图给别人留下深刻印象时，可能会失去自己的个人需求。
    这可能意味着“魅力者”很难不不断地炫耀和制造场面——即使很明显这在群体动态中并不需要。
    节选并翻译自 https://www.personalitydata.org/enneagram/type-3w2
    （注：如翻译质量不佳，请及时反映）
    """,
    # 3w4简介
    "3w4": """\
    第三型人被称为“成就者”，因为他们总是在寻找实现的方法，完成目标，努力实现这些目标，并让别人知道他们的成就。
    第四型人被称为“浪漫者”，因为他们总是寻找向他人表达自己的方式，让自己充满美丽，行事开放而诚实。
    四翼型人格将这些品质添加到了第三型人格中。
    这意味着 3w4 型人的目标是以竞争性和充满活力的方式实现目标，但主要关注自己作为个人以及如何实现和表达自己。
    这意味着他们最大的愿望是值得别人钦佩，从别人中脱颖而出，而他们最大的恐惧是做不到这一点。
    这可让九型人格3翼4个强大的个体也麻烦了。因此，3w4 型被称为“专业型”。 
    然而，与“成就者”不同，四翼型人可能更容易受到伤害，因为他们公开表达自己，而且他们可能更内向。
    他们会提出自己的意见或表达自己的才能和想法，即使是在没有正当理由或寻求的时刻，并且可能会在此过程中失去他人的同情或钦佩。
    这可能意味着“专业人士”很难不不断地炫耀和制造场面——即使很明显这在群体动态中并不需要。
    节选并翻译自 https://www.personalitydata.org/enneagram/type-3w4
    （注：如翻译质量不佳，请及时反映）
    """,
    # 4w3简介
    "4w3": """\
    第四型人被称为“浪漫者”，因为他们渴望独特，连接自己和世界的忧郁，以及他们对生活、爱情和工作理想的追求。
    第三型人因其注重形象、富有魅力、对进步的高能量追求而被称为“成就者”。
    三号翼型人通过成就来证明自己的特殊性，从而缓和了第四型人的自我专注，使他们比自然状态下更加专注于任务。
    这支队伍还将他们的戏剧性角色定制为更容易被社会接受但仍然独特的表现形式。
    由于他们能够在表现出不寻常甚至古怪的形象的同时取得高度成功，4w3 型被称为“贵族”。 
    然而，与“个人主义者”不同的是，4w3 可能会觉得他们为了通过捏造的形象获得成功，已经损害了核心类型所渴望的真实性。
    第四型人的内在匮乏感与第三型人光鲜亮丽的外表之间的紧张关系会造成深刻的认知失调，从而加剧第四型人固有的羞耻感和无价值感。
    节选并翻译自 https://www.personalitydata.org/enneagram/type-4w3
    （注：如翻译质量不佳，请及时反映）
    """,
    # 4w5简介
    "4w5": """\
    第四型人被称为“浪漫者”，因为他们渴望独特，连接自己和世界的忧郁，以及他们对生活、爱情和工作理想的追求。
    第五型人是“观察者”——创新的个人主义者，通常被视为超然且主要停留在思想领域。
    五号侧翼增强了第四型人本来就相当丰富的内心生活，但在健康的情况下，让他们更容易脱离自己的情绪，而不是认同它们。
    4w5 乐于保守自己和自己的内部对话，这常常给人冷漠、古怪或前卫的印象。因此，4w5 被称为“波西米亚人”。
    与核心第四型“浪漫者”或4w3“贵族”不同，4w5更有可能停止追求理想并陷入虚无主义的失败主义。
    他们可能对被理解和接受感到绝望，因此退缩到自己的世界里，尽管表面下情绪复杂，但看上去几乎是坚忍的。
    节选并翻译自 https://www.personalitydata.org/enneagram/type-4w5
    （注：如翻译质量不佳，请及时反映）
    """,
    # 5w4简介
    "5w4": """\
    第五型人，被称为“观察者”，是九型人格中最理智的类型。
    第四型人寻求培养人类体验的深度和高度的发自内心的体验。
    四号侧翼可以将第五型带入心脏中心。
    具有四号侧翼的第五型人更容易接触自己的情感（尽管他们仍然将自己的情感生活保持得非常私密），并且表达了对与伴侣和亲密朋友建立亲密联系的更深层次的需求。
    九型人格 5w4 类型的人像第五型人一样是出色的观察者和研究人员，但他们往往更具想象力和内省力，具有艺术或深奥的兴趣。
    这些孤独的创意者重视他们的个人隐私，很少关心社会对他们的看法。
    一些最伟大的文学作品和哲学见解都是由 5w4 完成的，但他们的沉默却常常阻碍他们与世界分享自己的贡献。
    节选并翻译自 https://www.personalitydata.org/enneagram/type-5w4
    （注：如翻译质量不佳，请及时反映）
    """,
    # 5w6简介
    "5w6": """\
    第五型人，孤独、理智、节俭，一生都在收集知识财富，以便他们能够过上简单的生活，而不依赖于别人。
    第六型人以社会群体和家庭的物质需求为导向，实用性很强。 
    5w6 不断发展实践技能和知识。九型人格 5w6 型寻求提供有用的信息和能力，以确保自己作为团体或团队中有价值的成员的地位。
    5w6 往往比其他五型人更具协作性，尽管他们担心让团队失望的基本恐惧常常使他们无法担任领导角色。
    这是最善于观察、最有条理、最善于分析的类型。
    5w6 人对任何情况都会采取冷静、理性的态度，他们热切地解决具有挑战性的问题，经常整合大多数人会忽视的重要细节（想想福尔摩斯）。
    节选并翻译自 https://www.personalitydata.org/enneagram/type-5w6
    （注：如翻译质量不佳，请及时反映）
    """,
    # 6w5简介
    "6w5": """\
    第六型人通常与父母、老板和其他生活中拥有权威的人有着复杂的关系。
    倾向于五号侧翼的第六型人相信，了解对他们的生活施加影响的人、系统和结构将帮助他们实现自主和安全。
    这种翼型被称为“捍卫者”，以认同并支持弱势群体而闻名。
    捍卫者相信要留意那些需要保护的人，防止那些人利用他们或滥用他们的权力。
    具有九型人格五号侧翼的第六型人格类型的人可能会过于关注权力的滥用，以至于他们的看法放大和扭曲了权威实际控制事件和情况的程度。
    结果，他们可能会低估自己的优势。
    许多著名的政治家和社会活动家都是具有五号侧翼的第六型人，其中一些人掌握着巨大的政治权力。
    尽管 6w5 在扩大弱势群体的权利方面取得了很大成就，但 6w5 领导人往往会采取严厉手段进行统治，因为他们倾向于夸大他们视为敌人的力量。
    节选并翻译自 https://www.personalitydata.org/enneagram/type-6w5
    （注：如翻译质量不佳，请及时反映）
    """,
    # 6w7简介
    "6w7": """\
    第六型人非常重视他们信任的人的建议和意见。
    他们相信两个头脑比一个头脑好，当他们能够信任一位诚实而有能力的领导者时，他们是最快乐的。
    第七型人往往是具有超凡魅力的影响者，他们通过激励他人帮助实现他们富有想象力的愿景来领导。
    与其他第六型人相比，具有第七翼的第六型人（有时被称为“伙伴”）在有很多让步的关系中更自在。
    朋友们经常借用第七型人不懈的积极态度来寻找一线希望。
    这是在他们的核心类型的更深层次特征之上分层的，并不能消除对被背叛或控制的核心恐惧。
    因此，九型人格 6w7 类型的人可能会表面上表达赞扬和渴望与人交朋友，但内心却对同事的动机感到怀疑和怀疑。
    任何第六型人的信任都是来之不易的，但一旦建立了情感纽带，6w7 型人就会以多种方式表达他们的忠诚，并且他们通常会要求经常保证他们的忠诚得到回报。
    这些类型的人相信友谊应该天长地久，当一段关系走到尽头时，一个好朋友可能很难接受事实。
    节选并翻译自 https://www.personalitydata.org/enneagram/type-6w7
    （注：如翻译质量不佳，请及时反映）
    """,
    # 7w6简介
    "7w6": """\
    第七型人追求迷人而有趣的经历，以此来分散自己对痛苦的注意力。
    拥有六号侧翼的第七型人通过让自己周围都是快乐的人来做到这一点。
    他们倾向于将自己隐藏的内心混乱投射到别人身上，并常常相信自己是圈子里真正快乐的人。
    绰号“艺人”的 7w6 人肩负着成为派对生命的严肃使命。
    艺人很少独处，他们是活跃的健谈者，他们很容易与各种各样的人建立联系，在他们进行的过程中进行匹配并建立桥梁。
    如果您想找到一辆 7w6，请看向节日人群的中心，并跟随欢乐的笑声。
    7w6 的亲密伙伴经历了一系列激动人心的冒险，然后精疲力竭地退出，想知道他们的 7w6 朋友在哪里找到继续前进的能量。
    这里面有一些疯狂和强迫的东西。艺人的笑容渐渐淡去，但没有动摇。
    当他们真的崩溃时，他们会陷入强烈的幻灭之中。
    没过多久，一些轻微的光芒就引起了他们的兴趣，他们重建了自己的世界，充满了有趣的乐趣，充满了朋友的娱乐。
    节选并翻译自 https://www.personalitydata.org/enneagram/type-7w6
    （注：如翻译质量不佳，请及时反映）
    """,
    # 7w8简介
    "7w8": """\
    第七型人顽皮而梦幻，而第八型人则脚踏实地。
    第七型人通常依靠他们的机智和创造性思维来创造他们想要的情况，而第八型人则依靠他们的力量和意志力，但两人在追求自己想要的东西时都很自信。
    所以九型人格 7w8 型是势不可挡的。 
    “现实主义者” 7w8 型通常比具有六号侧翼的第七型更加独立。
    他们的幽默可能非常另类，有时甚至很尖刻。他们追求物质上的成功，并且常常取得很高的成就。
    八型人坚韧的韧性赋予他们更厚的脸皮，让他们能够承担更大的风险，而不必担心受伤。
    他们不太关心别人的想法，尽管他们并不反对吸引那些欣赏他们无忧无虑的方式的人的注意。
    在决心实现目标的过程中，第七型人很容易合理化伤害他们认为阻碍他们的人。
    7w8 型人善于转移自己的注意力，不去后悔，但痛苦最终会追上他们——包括他们自己的痛苦，以及可能因阻碍他们而遭受痛苦的朋友、仰慕者和亲人的痛苦。
    节选并翻译自 https://www.personalitydata.org/enneagram/type-7w8
    （注：如翻译质量不佳，请及时反映）
    """,
    # 8w7简介
    "8w7": """\
    第八型人寻求具有挑战性的方式来发展自己的力量并展示自己的力量，以此来保护自己免受伤害。
    喜欢冒险的第七型人总是寻求新的体验。
    带有七号侧翼的八型人通常写为 8w7，是勇敢的冒险家，他们寻求具有挑战性的新体验并完成令人惊叹的壮举。
    他们既善于交际，又具有竞争力，常常会表现出尖锐的幽默感。特别是在年轻时和不健康的时候，他们喜欢通过恶作剧和戏弄来激怒别人。
    他们非常有兴趣了解别人是由什么组成的，他们觉得最好的方法就是找到他们最糟糕的一面。
    随着他们的成长和成熟，他们通常会了解到，对于大多数其他类型的人来说，这种行为会破坏而不是建立关系。 
    8w7 秉承第七型的魅力，通过阐明鼓舞人心的愿景、鼓励人们应对挑战并提供保护，吸引了一批忠实的追随者。
    他们渴望在世界上留下自己的印记，常常成为杰出的企业家、企业高管和政治领袖。
    有时，他们为了赢得忠诚和尊重而夸大外部威胁并做出超出其能力的承诺，从而陷入麻烦。
    九型人格的 8w7 往往比其他第八型人更冲动、更具对抗性和攻击性，后者具有其他邻居第九型人的特征。
    节选并翻译自 https://www.personalitydata.org/enneagram/type-8w7
    （注：如翻译质量不佳，请及时反映）
    """,
    # 8w9简介
    "8w9": """\
    保护型第八型人通常有着坚强的外表，但隐藏着一颗温柔的心。
    他们的快速愤怒常常掩盖了他们对失去纯真的悲伤，他们果断的行动往往是出于保护弱势群体的愿望。
    第九型人重视与周围人的深厚联系。他们为所关心的人的不同观点和价值观留出空间，以避免分离，并且在发生冲突时迅速达成和解。
    九型人格 8w9 型，散发着安静力量的感觉。它们可以被描述为力量的支柱和稳定的基石。
    他们说话时平静而庄重，冷静而自信，很容易让向他们寻求保护或建议的人放心。
    当他们感到受到威胁或怀疑时，他们的沉默有能力传达出压抑的愤怒或威胁性的忧郁。
    8w9 型可能看起来比其他第八型人更被动，但他们同样致力于保持控制。
    他们更喜欢在幕后指挥自己的事务，并且更容易出现被动的攻击行为。
    这种翼型不像其他八型翼型那么容易表现出令人生畏的愤怒。
    在极少数情况下，8w9 会发脾气，爆炸会更加突然、壮观和短暂。
    节选并翻译自 https://www.personalitydata.org/enneagram/type-8w9
    （注：如翻译质量不佳，请及时反映）
    """,
    # 9w8简介
    "9w8": """\
    9w8 与他们的和平缔造者同伴有很多相似之处，但由于受到八号侧翼的影响，他们在做出决定时更加自信和果断。
    他们仍然保持着第九型人的极度冷静的风度，但他们在做决定时更加相信自己的直觉，反过来觉得需要减少计划，因为他们知道一切最终都会成功。
    9w8 型人继承了第九型人对与他人联系的渴望，并且仍然以灵性寻求者而闻名。
    第九型人的这种优势融入了 9w8 型人，这使他们在建议他人在工作场所帮助他们时更加自信和直接。
    受到第八型人格的巨大影响，裁判的行为变得更加激进和顽固。
    他们比第九型人更具对抗性，这有时会导致他们无意中引发冲突。
    九型人格 9w8 型仍然希望避免冲突和他们知道对他们不利的情况。
    这就是为什么它们可以被视为极其矛盾的原因。
    凭借机翼引导，9w8 型更加自信、大胆和激励。
    他们仍在不断地寻求与世界的和平与和谐，但为了实现这一目标，他们更加努力。
    “你的团队的指导使你能够鼓励其他人，特别是那些工作没有得到足够赞扬的弱势群体。”
    节选并翻译自 https://www.personalitydata.org/enneagram/type-9w8
    （注：如翻译质量不佳，请及时反映）
    """,
    # 9w1简介
    "9w1": """\
    梦想家与他们的和平缔造者第九型人相似，但又截然不同。
    第九型人通常以友善、和蔼可亲、固执和矛盾着称。
    众所周知，9w1 型人比其他第九型人更有动力，而且他们会付出更多的努力来帮助有需要的人。
    然而，这也可能导致九型人格 9w1 型变得更加挑剔。
    和平缔造者非常害怕冲突，因此他们不惜一切代价避免陷入困境，而梦想家则更愿意竭尽全力帮助那些需要帮助的人。
    当谈到做决定时，9w1 型人在做决定时会受到直觉的驱使。
    这使他们能够在生活中创造秩序和常规，尤其是避免出现负面情绪的任何机会或情况。
    9w1 型人不断努力成为更好的自己，这可能会导致他们过于挑剔，永远不会认为自己“足够好”。
    当他们缺乏意识或判断力时，他们往往会愤怒地猛烈抨击。
    然而，如果有人认为自己做的事情在伦理或道德上是错误的，这种特殊的翼型并不害怕与他们对抗。
    九型人格的 9w1 往往比其他第九型人格的人具有更高的是非意识。
    9w1 与其核心第九型和平缔造者的许多特征相似，但在第一型的影响下，他们将自己更多地投入到世界中，以帮助更多的人并在整体上变得更好，尽管他们仍然害怕冲突。
    “受到一号侧翼的影响，九翼会出于道德考虑而进行谈判。”
    节选并翻译自 https://www.personalitydata.org/enneagram/type-9w1
    （注：如翻译质量不佳，请及时反映）
    """
}


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[DetectPrefix("!egram")]
    )
)
async def enneagram(app: Ariadne, group: Group, message: MessageChain = DetectPrefix("!egram")):
    if str(message) != "":
        await app.send_message(
            group,
            dedent(
                enneagram_list.get(
                    str(message).strip().lower(),
                    "找不到关于该九型人格类型的解释！"
                )
            )
        )
    else:
        await app.send_message(group, "输入!egram <类型>可查看关于该九型人格的解释！")
