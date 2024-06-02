import discord
from discord.ext import commands, tasks
import random
import os
import asyncio
from itertools import cycle

class RetornosSimples(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("RetornoSimples.py is ready")
        
    @commands.command()
    async def agarrar(self,ctx):
        await ctx.send(f"puxei alguem pra outro chat")
        
    @commands.command()
    async def bigtal(self,ctx):
        with open("Bot\Bot2\cogs\quack\gigtal.txt","r") as f:
            respostas_random = f.readlines()
            resposta = random.choice(respostas_random)
            await ctx.send(resposta)
    @commands.command()
    async def heylle(self,ctx):
        await ctx.send(f"A pedido de Heylle, a sato foi convocada, pra quê eu n sei")
    @commands.command()
    async def xedo(self,ctx):
        await ctx.send(f"Coé <@482324660525072415>, faz o curso")
    @commands.command()
    async def quack(self,ctx):
        with open("Bot\Bot2\cogs\quack\pato.txt","r") as f:
            respostas_random = f.readlines()
            resposta = random.choice(respostas_random)
            await ctx.send(resposta)
            
        
        
async def setup(client):
    await client.add_cog(RetornosSimples(client))