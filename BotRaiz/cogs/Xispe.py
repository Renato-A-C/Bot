import discord
from discord.ext import commands
import json
import os


class Xispe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file_path = "C:\Git\Bot\BotRaiz\cogs\jsonFiles\LEVEL.json"
        self.load_data()
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Nivelamento ta operacional.")


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

    
    async def on_message(self, message):
        if message.author.bot:
            return
        print(f"módulo xp {message.content}")
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

    @commands.command()
    async def level(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        member_id = str(member.id)
        if member_id in self.data['members']:
            xp = self.data['members'][member_id]['xp']
            level = self.data['members'][member_id]['level']
            await ctx.send(f"{member.mention} está no nível {level} com {xp} XP.")
        else:
            await ctx.send(f"{member.mention} ainda não tem XP registrado.")

async def setup(bot):
    await bot.add_cog(Xispe(bot))
