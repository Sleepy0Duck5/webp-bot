import os
import requests
import tempfile
import imghdr

from urllib.parse import urlparse

from webp_bot.converter.ffmpeg_converter import FFmpegConverter
from webp_bot.image import Image
from webp_bot.constants import Extensions


class Handler:
    def __init__(self) -> None:
        self._converter = FFmpegConverter()

    async def from_url(self, url: str) -> Image:
        file = self._download_file(url=url)

        original_filename = self._get_original_filename_from_url(url=url)

        extension = self._get_extension(filename=file.name, url=url)

        if extension in Extensions.REPLACE_EXTENSION:
            return Image(path=file.name, name=original_filename, extension="gif")
        elif extension in Extensions.WEBP_CONVERTABLE:
            return self._converter.convert(filepath=file.name)
        else:
            file.delete()
            raise Exception(f"Failed to convert webp image: {extension}")

    def _download_file(self, url: str):
        with tempfile.NamedTemporaryFile(delete=False) as f:
            response = requests.get(url=url)

            if response.status_code not in (200, 201):
                raise Exception(
                    f"Cannot get response from url={url}, status={response.status_code}, content={str(response.content)[:100]}"
                )

            f.write(response.content)
            f.flush()
            return f

    def _get_original_filename_from_url(self, url: str) -> str:
        parsed = urlparse(url)
        return os.path.basename(parsed.path)

    def _get_extension(self, filename: str, url: str) -> str:
        image_extension = imghdr.what(filename)

        if image_extension != None:
            return image_extension

        # maybe not a image
        parsed = urlparse(url)
        basename = os.path.basename(parsed.path)
        original_extension = basename.split(".")[-1]

        return original_extension
