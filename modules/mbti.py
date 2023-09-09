from graia.saya import Channel
from graia.saya.channel import ChannelMeta

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "MBTI"
channel.meta['description'] = "各MBTI类型解说"
channel.meta['author'] = "Abjust"