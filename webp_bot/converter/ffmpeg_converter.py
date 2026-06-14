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

    def convert_multiple(self, filepaths: list[str], is_image: bool = False) -> WebpImage:
        random_filename = uuid.uuid4().hex
        result_filepath = os.path.join(tempfile.tempdir, f"{random_filename}.webp")

        w, h = map(int, VideoConvertConfigs.SIZE.split("x"))
        
        streams = [
            ffmpeg.input(filename=filepath).filter('scale', w=w, h=h)
            for filepath in filepaths
        ]
        
        joined = ffmpeg.filter(streams, 'hstack', inputs=len(streams))

        if is_image:
            joined.output(
                result_filepath,
                vcodec="libwebp",
                lossless=1,
                vframes=1,
            ).run()
            extension = "gif"
        else:
            joined.filter(
                "fps", fps=VideoConvertConfigs.FPS
            ).output(
                result_filepath,
                vcodec="libwebp",
                lossless=1,
                loop=0,
                preset="default",
                an=None,
                vsync=0,
            ).run()
            extension = "webp"

        return WebpImage(path=result_filepath, name=random_filename, extension=extension)
