import discord
from discord.ext import commands, tasks
import random
import os
import asyncio
from itertools import cycle
client = commands.Bot(command_prefix=[".","*"], intents=discord.Intents.all())
# linha acima envolve inicio do bot, abaixo consta os status
bot_status = cycle(["eu","quero","GANHAR DINHEIRO SEM TRABALHARRRRR"])
# troca de status no metodo abaixo
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))
    
@client.event
async def on_ready():
    print("Bot conectado")
# ctx.send envia mensagem, 
# ctx.author.send , para quem usou o comando diretamente
#@client.command()
#async def ping(ctx):
#    await ctx.send("a")
    
#@client.command(aliases=["quaestio"])
#async def pergunte(ctx, * , questao):
#    with open("prirepo/Bot/Bot2/cogs/respostas.txt","r") as f:
#        respostas_random = f.readlines()
#        resposta = random.choice(respostas_random)
#        
#        await ctx.send(resposta)
    
@client.command(aliases=["quem"])
async def on_message(ctx):
    await ctx.send("te perguntou?")
    
async def load():
    for filename in os.listdir("prirepo\Bot\Bot2\cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            
async def main():
    async with client:
        await load()
        await client.start("MTA0MzAxMTY2Mzc0MzQyNjYyMg.GUADCe.Axu9ziWGTWKZidyxGJ9U2VFOB1p254LbHcO__Y")
    
asyncio.run(main())