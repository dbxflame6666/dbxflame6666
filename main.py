import discord
from discord.ext import command

intents = discord.Intents.all()
token = "YOUR TOKEN"

client = commands.Bot(
  command_prefix = ".",
  help_command = None,
  intents = intents
  )

@client.event
async def on_ready():
  print(f"{client.user}{client.user.id} is ready!")
  
  
  
client.run(token)
