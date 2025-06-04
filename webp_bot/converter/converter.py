from abc import ABCMeta

from webp_bot.image import Image


class Converter(metaclass=ABCMeta):
    def convert(self, filepath: str) -> Image:
        raise NotImplementedError
