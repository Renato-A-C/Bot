import discord
from discord.utils import get
from discord.ext import commands, tasks
import random
import os
import asyncio
from itertools import cycle
import json
from Valor import Valor
#import ValorToken
client = commands.Bot(command_prefix=[".","*"], intents=discord.Intents.all())
@client.event
async def on_ready():
    print("Bot conectado")
####### 

async def load():
    for filename in os.listdir("C:\Git\Bot\Bot2\cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

chave = Valor(valor="ativo")
chaas= chave._pegarToken()
async def main():
    async with client:
        await load()
        await client.start(chaas)

 
        
@client.command(aliases=["quem"])
async def on_message(ctx):
    await ctx.send("te perguntou?")
    
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("deu erro, falta argumentos")    
asyncio.run(main())

# ctx.send envia mensagem, 
# ctx.author.send , para quem usou o comando diretamente
#@client.command()
#async def ping(ctx):
#    await ctx.send("a")
#@client.tree.command(name="ping", description="mostra latencia")
#async def ping(interaction:discord.Interaction):
#    bot_latency = round(client.latency*1000)
#    await interaction.response.send_message(f"pong! {bot_latency} ms.")
