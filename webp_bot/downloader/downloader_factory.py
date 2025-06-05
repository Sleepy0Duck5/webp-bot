from webp_bot.downloader.downloader import Downloader
from webp_bot.downloader.dccon_downloader import DcconDownloader
from webp_bot.downloader.general_downloader import GeneralDownloader


class DownloaderFactory:
    def create(self, url: str) -> Downloader:
        if url.startswith("https://dcimg"):
            return DcconDownloader()

        return GeneralDownloader()
