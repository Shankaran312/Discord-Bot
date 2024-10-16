import discord
from discord.ext import commands

# Replace 'YOUR_TOKEN_HERE' with your actual Discord bot token
TOKEN = 'YOUR_TOKEN_HERE'

# Define intents
intents = discord.Intents.default()
intents.messages = True  # Enable the messages intent

# Set up the bot with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event that triggers when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

# Command to respond to
@bot.command()
async def hello(ctx):
    await ctx.send('Hello! 👋 How can I assist you today?')

# Command to ping the bot
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! 🏓')

# Run the bot
bot.run(TOKEN)
