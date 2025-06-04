from webp_bot.image import WebpImage

from webp_bot.converter.converter import Converter


class FFmpegConverter(Converter):
    def convert(self, filepath: str) -> WebpImage:
        pass
