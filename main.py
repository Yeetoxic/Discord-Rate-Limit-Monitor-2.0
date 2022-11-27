import os, discord

from DRLM2 import DRLM2
DRLM2()


client = discord.Client()

@client.event
async def on_ready():
    print("We gud 2 go!")
    print(f"logged in as: {client.user}")

token = os.environ.get("SECRET_BOT_TOKEN")
client.run(token)