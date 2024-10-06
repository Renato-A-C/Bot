import discord
from discord.ext import commands
import asyncio
import json
from Valor import Valor
import random
import os
# inicializador
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=[".", "*"], intents=discord.Intents.all())
        self.initial_extensions = ["cogs.commandoP", "cogs.commandoS", "cogs.ticket_cog", "cogs.Embed","cogs.tempo","cogs.repetir", "cogs.moderarv2S","cogs.moderarv2P","cogs.Xispe"]
        self.synced = False
        self.file_path = "C:\Git\Bot\BotRaiz\cogs\jsonFiles\LEVEL.json"
        self.load_data()
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
         

    
    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {"members": {}}

    def save_data(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_xp(self, member_id, xp_to_add):
        if member_id not in self.data['members']:
            self.data['members'][member_id] = {"xp": 0, "level": 1}

        self.data['members'][member_id]['xp'] += xp_to_add
        self.save_data()

    # módulos para reação a mensagens   
    async def on_message(self, message):
        if message.author == self.user:
            return
        opcao = ["Sim", "Não"]
        trigger_word = "quem"
        gatilho2 = "paia"
        gatilho3= "isso é feito no céu?"
        print(f"{message.content}")
        if trigger_word in message.content.lower() and message.content.lower().startswith(trigger_word):
            print(f"Recebi uma mensagem: {message.content}")
            await message.channel.send(f"TE PERGUNTOU")
            
        elif gatilho2 in message.content.lower() and message.content.lower().startswith(gatilho2):
            print(f"Recebi uma mensagem: {message.content}")
            await message.channel.send(f"paiado")
            
        elif gatilho3 in message.content.lower() and message.content.lower().startswith(gatilho3):
            print(f"Recebi uma mensagem: {message.content}")
            await message.channel.send(f"{random.choice(opcao)}")
        
        if message.author.bot:
            return

        member_id = str(message.author.id)
        message_length = len(message.content)

        # Calculando XP
        xp_to_add = 1 + (message_length // 10)

        # Adiciona XP
        self.add_xp(member_id, xp_to_add)

        # (Opcional) Verifica o nível atual e aumenta se necessário
        current_xp = self.data['members'][member_id]['xp']
        current_level = self.data['members'][member_id]['level']

        # Exemplo simples de cálculo de nível
        next_level_xp = 100 * current_level
        if current_xp >= next_level_xp:
            self.data['members'][member_id]['level'] += 1
            await message.channel.send(f"{message.author.mention} subiu para o nível {current_level + 1}!")
            self.save_data()
        await self.process_commands(message)
    
async def main():
    chave = Valor(valor="ativo")
    chaas = chave._pegarToken()

    bot = MyBot()

    async with bot:
        await bot.start(chaas)

asyncio.run(main())
