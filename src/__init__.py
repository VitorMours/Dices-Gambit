import discord
import logging
import discord
from discord.ext import commands

from .utils import log





class DiscordBot(commands.Bot):
    def __init__(self, intents) -> None:

        super().__init__(command_prefix="++",
                         intents=intents,
                         description="D&D bot for players and masters")

        log.create_logger()
        self.log = logging.getLogger(__name__)
        self.log.debug("testando")


    async def on_connect(self):
        self.log.info(f"Connected to discord API via: {self.user} - {self.user.id}")
    
    async def on_ready(self):
        self.log.info(f"Connected to the server and ready to serve")
    
    async def on_message(self, message):
        self.log.debug(f"{message.author.name} message: {message.content}")    
        await self.process_commands(message)




if __name__ == "__main__":
    bot = DiscordBot()
    bot.run()















