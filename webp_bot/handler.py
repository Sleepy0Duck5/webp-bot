import requests
import tempfile

from webp_bot.converter.image_converter import ImageConverter


class Handler:
    def __init__(self) -> None:
        self._image_converter = ImageConverter()

    async def from_url(url: str):
        image = requests.get(url=url)
        
