import discord
from discord.ext import commands, tasks
import random
import os






intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '*', intents = intents)

gamelist = []


# @client.event
# async def on_ready():
#     print("Bot is ready")

# @client.event
# async def on_member_join(member):
#     print(f'{member} has joined a server.')
#
# @client.event
# async def on_member_remove(member):
#     print(f"{member} has left the server.")

# @client.command()
# async def ping(ctx):
#     await ctx.send(f"PONG!{round(client.latency * 1000)}ms")

# @client.command(aliases = ["8ball","test"])
# async def _8ball(ctx,*,question):
#     responses = ["It is certain.",
#                 "It is decidedly so.",
#                 "Without a doubt.",
#                 "Yes - definitely.",
#                 "You may rely on it.",
#                 "As I see it, yes.",
#                 "Most likely.",
#                 "Outlook good.",
#                 "Yes.",
#                 "Signs point to yes.",
#                 "Reply hazy, try again.",
#                 "Ask again later.",
#                 "Better not tell you now.",
#                 "Cannot predict now.",
#                 "Concentrate and ask again.",
#                 "Don't count on it.",
#                 "My reply is no.",
#                 "My sources say no.",
#                 "Outlook not so good.",
#                 "Very doubtful."
#                 ]
#     await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
#
# @client.command()
# async def clear(ctx, amount=5):
#     await ctx.channel.purge(limit = amount)

# @client.command()
# async def load(ctx, extension):
#     client.load_extension(f"cogs.{extension}")
#
# @client.command()
# async def unload(ctx, extension):
#     client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')



client.run('ODM3MjUxODk5NTUwOTkwMzU3.YIp1mA.ROXvhtNbZUQXOY87JPiHRfhiup0')

