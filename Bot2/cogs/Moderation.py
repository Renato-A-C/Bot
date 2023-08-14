import discord
from discord.ext import commands, tasks
import random
import os
import asyncio
from itertools import cycle

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderaçao.py is ready")
        
    @commands.command()
    @commands.has_permissions()
    async def clear(self,ctx, count: int):
        if (count >100):
            await ctx.send(embed = discord.Embed(color=discord.Color.red(), title=f"My limit is 100 message"))
        if (count<=100) and (count>0):
            await ctx.channel.purge(limit=count+1)
            await ctx.send(f"No total, {count} mensagens foram apagadas")
        else:
            await ctx.send(f"Primeiro coloque um número válido")
    @commands.command()
    @commands.has_permissions()
    async def kick(self,ctx,member: discord.Member, modreason):
        await ctx.guild.kick
    
async def setup(client):
    await client.add_cog(Moderation(client))