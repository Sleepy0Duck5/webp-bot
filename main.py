import os


from dotenv import load_dotenv
from webp_bot.webp_bot import WebpBot


def init() -> None:
    load_dotenv(verbose=True)
    bot_token = os.getenv("BOT_TOKEN")

    bot = WebpBot(bot_token=bot_token)

    bot.run()


if __name__ == "__main__":
    init()
