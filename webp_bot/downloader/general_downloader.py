import tempfile
import requests

from webp_bot.downloader.downloader import Downloader


class GeneralDownloader(Downloader):
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
