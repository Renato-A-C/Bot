import discord
from discord.ext import commands, tasks
import random
import os
import asyncio
from itertools import cycle

class Pergunte(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("Pergunte.py is ready")

    @commands.command()
    async def pergunte(self, ctx, * , questao):
        with open("prirepo/Bot/Bot2/cogs/respostas.txt","r") as f:
            respostas_random = f.readlines()
            resposta = random.choice(respostas_random)
        
            await ctx.send(resposta)
            
async def setup(client):
    await client.add_cog(Pergunte(client))