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

    def create_embed(self, title, description, ctx):
        embed_message = discord.Embed(
            title=title,
            description=description,
            color=discord.Color.blue()
        )
        embed_message.set_author(
            name=f"Requested by {ctx.author}",
            icon_url=ctx.author.avatar.url
        )
        embed_message.set_thumbnail(url=ctx.guild.icon.url)
        embed_message.set_image(url=ctx.guild.icon.url)
        embed_message.set_footer(
            text="Este é o rodapé",
            icon_url=ctx.author.avatar.url
        )
        return embed_message
    
    @commands.command()    
    async def embed(self, ctx):
        embed_message = self.create_embed(
            title="Título da Embed",
            description="Descrição da Embed",
            ctx=ctx
        )
        embed_message.add_field(name="Nome do campo", value="Valor do campo", inline=False)
        
        await ctx.send(embed=embed_message)
    
async def setup(client):
    await client.add_cog(Embed(client))