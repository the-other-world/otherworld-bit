from graia.saya import Channel
from graia.saya.channel import ChannelMeta

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "九型人格"
channel.meta['description'] = "各九型人格类型解说"
channel.meta['author'] = "Abjust"