import os
import tempfile
import ffmpeg
import uuid

from webp_bot.image import WebpImage
from webp_bot.converter.converter import Converter
from webp_bot.constants import VideoConvertConfigs


class FFmpegConverter(Converter):
    def convert(self, filepath: str) -> WebpImage:
        random_filename = f"{uuid.uuid4().hex}.webp"
        result_filepath = os.path.join(tempfile.tempdir, random_filename)

        ffmpeg.input(filename=filepath).filter(
            "fps", fps=VideoConvertConfigs.FPS
        ).output(
            result_filepath,
            vcodec="libwebp",
            lossless=1,
            loop=0,
            preset="default",
            an=None,
            vsync=0,
            s=VideoConvertConfigs.SIZE,
        ).run()

        return WebpImage(path=result_filepath, name=random_filename, extension="webp")
