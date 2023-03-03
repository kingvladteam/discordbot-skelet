import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'hello' in message.content.lower():
        await message.channel.send('Hello there!')

    if 'bye' in message.content.lower():
        await message.channel.send('Goodbye!')

client.run(os.getenv('DISCORD_TOKEN'))
