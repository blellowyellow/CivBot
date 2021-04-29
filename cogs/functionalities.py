import discord
from discord.ext import commands, tasks
from classes.game import Game
from civbot import gamelist

class Functionalities(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def create(self, ctx, name, playdate):
        game = Game(ctx.message.author, name, playdate)
        gamelist.append(Game)
        await ctx.send(game.get_name() + " " + game.get_author() + " " + game.get_playdate() + " " + game.id)












def setup(client):
    client.add_cog(Functionalities(client))