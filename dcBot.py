import discord
from discord import app_commands
from discord.ext import commands
import random
class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id=1042560674812923914))
            self.synced = True
        print(f"Entramos como {self.user}.")
        
client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name= "teste", description = "testando", guild = discord.Object(id = 1042560674812923914))
async def self(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f"Olá {name}! eu fui feito a base do Discord.py")   
     
@tree.command(name= "surra", description = "em alguém", guild = discord.Object(id = 1042560674812923914))
async def self(interaction: discord.Interaction, atacante: str, atacado: str, objeto:str, tempo:float):
    if type(tempo) != float:
        await interaction.response.send_message(f"comando errado, o tempo deve ser apenas numérico")
    else:
        await interaction.response.send_message(f"Por pedido de {atacante}, o alvo {atacado} vai levar uma surra de {objeto} por {tempo} minutos")
    

@tree.command(name="calculadora", description="calcula algo",guild = discord.Object(id = 1042560674812923914))
@app_commands.describe(operacoes='tipos de operações')
@app_commands.choices(operacoes=[
    discord.app_commands.Choice(name='vezes',value=1),
    discord.app_commands.Choice(name='divisao',value=2),
    discord.app_commands.Choice(name='subtraçao',value=3),
    discord.app_commands.Choice(name='adiçao',value=4)
])
async def self(interaction: discord.Interaction,primeiro_numero:float,operacoes:discord.app_commands.Choice[int], segundo_numero:float):
    
    if operacoes.name == "vezes":
        resultado = primeiro_numero*segundo_numero
        await interaction.response.send_message(f" a resposta é {resultado}")
    elif operacoes.name == "divisao":
        resultado = primeiro_numero/segundo_numero
        await interaction.response.send_message(f" a resposta é {resultado}") 
    elif operacoes.name == "subtraçao":
        resultado = primeiro_numero-segundo_numero
        await interaction.response.send_message(f" a resposta é {resultado}") 
    elif operacoes.name == "adiçao":
        resultado = primeiro_numero+segundo_numero
        await interaction.response.send_message(f" a resposta é {resultado}") 
        


client.run("MTA0MzAxMTY2Mzc0MzQyNjYyMg.GJ4MKs.vE89gFLabLaRapK-9wGKFcUM_cObiuI8A8pU5Q")