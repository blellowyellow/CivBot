import discord
from discord.ext import commands, tasks
from itertools import cycle

status = cycle(["Cizmina stara", "Tomas je mala pickica", "mimi losa zemlja mimi"])

class Main(commands.Cog):

    def __init__(self, client):
        self.client = client

    #EVENTS
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready")
        self.change_status.start()
        await self.client.change_presence(status=discord.Status.online)

    @commands.command()
    async def clear(ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    #TASKS
    @tasks.loop(seconds=10)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Game(next(status)))


def setup(client):
    client.add_cog(Main(client))