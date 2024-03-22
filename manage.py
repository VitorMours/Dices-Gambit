import discord
import src

from src import DiscordBot
from src.utils import log







if __name__ == "__main__":
   
    from dotenv import dotenv_values
    

    intents = discord.Intents.all()
    bot = DiscordBot(intents)

    configs=dotenv_values(".env")
    bot.run(configs["TOKEN"])

