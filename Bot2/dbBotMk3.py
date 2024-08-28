import discord
from discord.ext import commands
import asyncio
import json
from Valor import Valor
import random
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=[".", "*"], intents=discord.Intents.all())
        self.initial_extensions = ["cogs.commandoP", "cogs.commandoS", "cogs.ticket_cog", "cogs.Embed","cogs.tempo","cogs.repetir", "cogs.moderarv2S","cogs.moderarv2P"]
        self.synced = False

    async def setup_hook(self):
        for ext in self.initial_extensions:
            await self.load_extension(ext)

        if not self.synced:
            guild = discord.Object(id="571722603920752650")  # Substitua pelo ID do seu servidorguild=guild
            await self.tree.sync()
            self.synced = True  # Marcar que a sincronização foi feita
            print("Comandos sincronizados com sucesso com a guilda.")

    async def on_ready(self):
        print(f"Bot conectado como {self.user}")

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("deu erro")
            
    async def on_message(self, message):
        if message.author == self.user:
            return
        opcao = ["Sim", "Não"]
        trigger_word = "quem"
        gatilho2 = "paia"
        gatilho3= "isso é feito no céu?"
        if trigger_word in message.content.lower() and message.content.lower().startswith(trigger_word):
            print(f"Recebi uma mensagem: {message.content}")
            await message.channel.send(f"TE PERGUNTOU")
            
        elif gatilho2 in message.content.lower() and message.content.lower().startswith(gatilho2):
            print(f"Recebi uma mensagem: {message.content}")
            await message.channel.send(f"paiado")
            
        elif gatilho3 in message.content.lower() and message.content.lower().startswith(gatilho3):
            print(f"Recebi uma mensagem: {message.content}")
            await message.channel.send(f"{random.choice(opcao)}")
        await self.process_commands(message)

async def main():
    chave = Valor(valor="ativo")
    chaas = chave._pegarToken()

    bot = MyBot()

    async with bot:
        await bot.start(chaas)

asyncio.run(main())
