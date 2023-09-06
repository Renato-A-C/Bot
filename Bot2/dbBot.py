import discord
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
@client.event
async def on_guild_join(guild):
    with open("cogs\jsonFiles\mutes.json","r") as f:
        mute_role = json.load(f)
        
        mute_role[str(guild.id)] = None
        
    with open("cogs\jsonFiles\mutes.json","w") as f:
        json.dump(mute_role, f, indent=4)
###########  
@client.event
async def on_guild_remove(guild):
    with open("cogs\jsonFiles\mutes.json","r") as f:
        mute_role = json.load(f)
        
        mute_role.pop(str(guild.id))
        
    with open("cogs\jsonFiles\mutes.json","w") as f:
        json.dump(mute_role, f, indent=4)

async def load():
    for filename in os.listdir(".\Bot\Bot2\cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

chave = Valor(valor="ativo")
chaas= chave._pegarToken()
async def main():
    async with client:
        await load()
        await client.start(chaas)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("deu erro, falta argumentos")
@client.command(aliases=["quem"])
async def on_message(ctx):
    await ctx.send("te perguntou?")
    
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
