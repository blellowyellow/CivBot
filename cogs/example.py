import discord
from discord.ext import commands, tasks
from itertools import cycle


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    # #EVENT
    # @commands.Cog.listener()
    # async def on_reaction_add(self, reaction, user,ctx):
    #     channel = reaction.message.channel
    #     await ctx.send_message(channel, "{} has added {} to the message".format(user.name, reaction.emoji, reaction.message.content))
    #
    # @commands.Cog.listener()
    # async def on_reaction_remove(self, reaction, user,ctx):
    #     channel = reaction.message.channel
    #     await ctx.send_message(channel, "{} has removed {} from the message".format(user.name, reaction.emoji, reaction.message.content))
    #
    # #COMMAND
    # @commands.command()
    # async def ping(self, ctx):
    #     await ctx.send("PONG")
    #
    # @commands.command()
    # async def displayembed(self, ctx):
    #     embed = discord.Embed(
    #         title = 'Title',
    #         description = "This is a description",
    #         colour = discord.Colour.red()
    #     )
    #
    #     embed.set_footer(text = 'FOOTER')
    #     await ctx.send(embed=embed)







def setup(client):
    client.add_cog(Example(client))
