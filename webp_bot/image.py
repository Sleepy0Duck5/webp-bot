import os
from loguru import logger


class Image:
    def __init__(self, path: str, name: str, extension: str) -> None:
        self._path = path
        self._name = name
        self._extension = extension

    def get_bytes(self) -> bytes:
        with open(self._path, "rb") as f:
            return f.read()

    def get_path(self) -> str:
        return self._path

    def get_name(self) -> str:
        return self._name + "." + self._extension

    def delete(self) -> str:
        if os.path.exists(self._path):
            try:
                os.remove(self._path)
            except Exception as e:
                logger.opt(exception=e).exception(
                    f"Failed to delete temporary file: {self._path}"
                )


class WebpImage(Image):
    pass
