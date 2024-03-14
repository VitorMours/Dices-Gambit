import discord
import logging
intents = discord.Intents.all()

client = discord.Client(intents=intents)




@client.event 
async def on_connect():
    print(f"Connected to discord API")

@client.event
async def on_ready():
    print(f"User: {client.user}")
    

















