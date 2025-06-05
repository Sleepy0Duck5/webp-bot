import tempfile
import requests

from webp_bot.downloader.downloader import Downloader
from webp_bot.constants import DCinside


class DcconDownloader(Downloader):
    def _download_file(self, url: str) -> tempfile._TemporaryFileWrapper:
        with tempfile.NamedTemporaryFile(delete=False) as f:
            session = requests.Session()
            dccon_img_request = session.post(
                url,
                headers={"X-Requested-With": "XMLHttpRequest", "type": "image"},
                # headers={
                #     "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                #     "referer": DCinside.REFERER,
                #     "host": "dcimg5.dcinside.com",
                #     "Sec-Fetch-Dest": "image",
                #     "Sec-Fetch-Mode": "no-cors",
                #     "Sec-Fetch-Site": "same-site",
                # },
            )

            f.write(dccon_img_request.content)
            f.flush()
            return f
