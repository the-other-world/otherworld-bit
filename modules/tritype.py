from graia.saya import Channel
from graia.saya.channel import ChannelMeta

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "Tritype"
channel.meta['description'] = "各九型人格Tritype类型解说"
channel.meta['author'] = "Abjust"