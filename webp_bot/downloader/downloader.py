import os
import tempfile
from urllib.parse import urlparse


class Downloader:
    def download_file(self, url: str) -> tempfile._TemporaryFileWrapper:
        if not self._validate_url(url=url):
            raise Exception(f"Invalid url({url})")

        return self._download_file(url=url)

    def _validate_url(self, url: str) -> bool:
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except AttributeError:
            return False

    def _download_file(self, url: str) -> tempfile._TemporaryFileWrapper:
        raise NotImplementedError

    def get_original_filename_from_url(self, url: str) -> str:
        parsed = urlparse(url)
        return os.path.basename(parsed.path)
