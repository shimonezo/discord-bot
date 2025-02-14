import discord
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot is ready! Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if isinstance(message.channel, discord.DMChannel):  # چک کردن پیام در دایرکت
        if message.content.lower() == "hello":
            await message.channel.send("Hello! How can I help you?")
        else:
            await message.channel.send("I received your message!")

# دریافت توکن از متغیر محیطی
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if TOKEN is None:
    print("Error: DISCORD_BOT_TOKEN is not set. Please set the environment variable.")
else:
    client.run(TOKEN)
