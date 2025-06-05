import os
import requests
import tempfile
import imghdr
from urllib.parse import urlparse

from webp_bot.converter.ffmpeg_converter import FFmpegConverter
from webp_bot.downloader.downloader_factory import DownloaderFactory

from webp_bot.downloader.downloader import Downloader
from webp_bot.image import Image
from webp_bot.constants import Extensions


class Handler:
    def __init__(self) -> None:
        self._converter = FFmpegConverter()
        self._downloader_factory = DownloaderFactory()

    async def from_url(self, url: str) -> Image:
        downloader: Downloader = self._downloader_factory.create(url=url)

        file = downloader.download_file(url=url)

        original_filename = downloader.get_original_filename_from_url(url=url)

        extension = self._get_extension(filename=file.name, url=url)

        if extension in Extensions.REPLACE_EXTENSIONS:
            return Image(path=file.name, name=original_filename, extension="gif")
        elif extension in Extensions.WEBP_CONVERTABLE:
            return self._converter.convert(filepath=file.name)
        else:
            if file:
                Image(path=file.name, name=original_filename, extension="gif").delete()
            raise Exception(f"Failed to convert webp image: {extension}")

    def _download_file(self, url: str) -> tempfile._TemporaryFileWrapper:
        with tempfile.NamedTemporaryFile(delete=False) as f:
            response = requests.get(url=url)

            if response.status_code not in (200, 201):
                raise Exception(
                    f"Cannot get response from url={url}, status={response.status_code}, content={str(response.content)[:100]}"
                )

            f.write(response.content)
            f.flush()
            return f

    def _get_extension(self, filename: str, url: str) -> str:
        image_extension = imghdr.what(filename)

        if image_extension != None:
            return image_extension

        # maybe not a image
        parsed = urlparse(url)
        basename = os.path.basename(parsed.path)
        original_extension = basename.split(".")[-1]

        if len(original_extension) > 4:
            for extension in Extensions.SUPPORTED_EXTENSIONS:
                if extension in url.lower():
                    return extension

            raise Exception("Failed to find original extension from url")

        return original_extension
