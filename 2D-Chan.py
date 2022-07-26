import discord
from discord.ext import commands
from config import *

bot = commands.Bot(command_prefix='>')
client = discord.Client()
censured = ['сука', 'бля', 'пидор']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for cen in censured:
        if cen in message.content.lower():
            await message.channel.send(f'Не матерись, @{message.author.name}, тут дети)')


client.run(TOKEN)
bot.run(TOKEN)