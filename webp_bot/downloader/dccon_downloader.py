import tempfile
import urllib

from webp_bot.downloader.downloader import Downloader
from webp_bot.constants import DCinside


class DcconDownloader(Downloader):
    def _download_file(self, url: str) -> tempfile._TemporaryFileWrapper:
        with tempfile.NamedTemporaryFile(delete=False) as f:
            con_url = urllib.request.Request(url)
            con_url.add_header("Referer", DCinside.REFERER)
            con_file = urllib.request.urlopen(con_url)

            f.write(con_file.read())
            f.flush()
            return f
