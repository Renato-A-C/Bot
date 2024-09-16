import discord; from discord import *
from discord.ext import commands, tasks
import random
import os
import asyncio
from itertools import cycle

class Embed(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("Embed.py is ready")

    @commands.command()
    async def embed(self, ctx):
        embed_message = discord.Embed(title="Título da embed",description="Descrição da embed",color=discord.Color.blue())
        embed_message.set_author(name=f"requested by {ctx.author}", icon_url=ctx.author.avatar)
        embed_message.set_thumbnail(url=ctx.guild.icon)
        embed_message.set_image(url=ctx.guild.icon)
        embed_message.add_field(name="Nome do campo", value="Valor do campo", inline=False)
        embed_message.set_footer(text="este é o rodapé",icon_url=ctx.author.avatar)
        
        await ctx.send(embed= embed_message) 
            
async def setup(client):
    await client.add_cog(Embed(client))