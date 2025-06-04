import discord


from discord.ext import commands
from discord import app_commands
from loguru import logger

from webp_bot.handler import Handler


class WebpBot:
    """
    Wrap discord bot instances, and handling events for what to do.
    """

    def __init__(self, bot_token: str) -> None:
        intents = discord.Intents.default()
        # intents.message_content = True

        self._bot_token = bot_token
        self._bot = commands.Bot(command_prefix="!", intents=intents)

        self._handler = Handler()

        self._define_events()

    def _define_events(self) -> None:
        """
        Define discord application commands
        """

        @self._bot.tree.command(
            name="from_url", description="Convert URL based images into webp"
        )
        @app_commands.describe(url="URL")
        async def from_url(interaction: discord.Interaction, url: str) -> None:
            await interaction.response.send_message("processing...", ephemeral=True)

            await self._handler.from_url(url=url)

            await interaction.response.send_message(f"error raised", ephemeral=True)

            # await interaction.followup.send(file=discord.File(f, temp_video_id+".gif"))

        @self._bot.event
        async def on_ready() -> None:
            """
            Sync slash commands to discord server
            """
            try:
                await self._bot.tree.sync()
                logger.info("Bot ready")
            except Exception as e:
                logger.opt(e).error("Failed to ready slash commands")

    def run(self) -> None:
        self._bot.run(token=self._bot_token)
