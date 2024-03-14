import discord
import src
from src import client


intents = discord.Intents.all()






if __name__ == "__main__":

    from dotenv import dotenv_values
    configs=dotenv_values(".env")
    client.run(configs["TOKEN"])


