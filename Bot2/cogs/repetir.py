import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta

class repetir(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mensagem_repetida.start()  # Inicia a tarefa quando a Cog é carregada

    @tasks.loop(minutes=60)  # Define o intervalo de tempo para o loop
    async def mensagem_repetida(self):
        canal = self.bot.get_channel(1014902935840374834)  # Substitua YOUR_CHANNEL_ID pelo ID do canal
        if canal:
            await canal.send("GG rapeize, Z0n4 voltando pros 6k")
            #await canal.send("Já pensaram em divulgar o Z0n4? Utilize convites próprios e a cada 10 usos você irá ganhar alguma recompensa")
        else:
            print("Canal não encontrado.")
            
    @tasks.loop(minutes=155)  # intervalo de tempo
    async def mensagem_repetida(self):
        canal = self.bot.get_channel(1014902935840374834)  # id de canal
        if canal:
            await canal.send("Independente irmão, é culpa do dope")
            #await canal.send("Já pensaram em divulgar o Z0n4? Utilize convites próprios e a cada 10 usos você irá ganhar alguma recompensa")
        else:
            print("Canal não encontrado.")

    @mensagem_repetida.before_loop
    async def before_mensagem_repetida(self):
        await self.bot.wait_until_ready()  # Espera o bot estar pronto antes de começar a tarefa

async def setup(bot):
    await bot.add_cog(repetir(bot))