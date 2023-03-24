import discord
import datetime
import math
from discord import app_commands
from discord.ext import commands
import random
#z0n4 571722603920752650
#ads 1042560674812923914
class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id=581572127501713411))
            self.synced = True
        print(f"Entramos como {self.user}.")
        
client = abot()
tree = app_commands.CommandTree(client)
@tree.command(name= "teste", description = "testando", guild = discord.Object(id = 581572127501713411))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"Olá! eu fui feito a base do Discord.py . Sim eu tô funcionando :thumbsup:")   

@tree.command(name= "pergunte", description = "e o bot responde", guild = discord.Object(id = 581572127501713411))
async def self(interaction: discord.Interaction, pergunta: str):
    respostas= ["não sei", "quem sabe","se eu soubesse eu te falava","não :)","a va ti lascar rapa","Sim","para com issae bicho"]
    await interaction.response.send_message(f"**Pergunta: **{pergunta}\n**Resposta**: {random.choice(respostas)}")   

@tree.command(name="randomfoto",description="acha uma foto ae",guild = discord.Object(id = 581572127501713411))
async def get_random_image(img):
    
    num= random.randint(0, 1920)    
    Embed = discord.Embed(
        title="Foto buscada com sucesso",
        description="Lembrando q é random msm",
        color=discord.Color.random(),
        
        )
    Embed.set_image(url="https://api.lorem.space/image?w=1920&h=1080")
    await img.channel.send(embed=Embed)
@tree.command(name= "surra", description = "em alguém", guild = discord.Object(id = 581572127501713411))
async def self(interaction: discord.Interaction, atacante: str, atacado: str, objeto:str, tempo:float):
    if type(tempo) != float:
        await interaction.response.send_message(f"comando errado, o tempo deve ser apenas numérico")
    else:
        await interaction.response.send_message(f"Por pedido de {atacante}, o alvo {atacado} vai levar uma surra de {objeto} por {round(tempo)} minutos")
    

@tree.command(name="calculadora", description="calcula algo",guild = discord.Object(id = 581572127501713411))
@app_commands.describe(operacoes='tipos de operações')
@app_commands.choices(operacoes=[
    discord.app_commands.Choice(name='vezes',value=1),
    discord.app_commands.Choice(name='divisao',value=2),
    discord.app_commands.Choice(name='subtraçao',value=3),
    discord.app_commands.Choice(name='adiçao',value=4),
    discord.app_commands.Choice(name='porcentagem',value=5)
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



client.run("MTA0MzAxMTY2Mzc0MzQyNjYyMg.G6YCZ6.uJgUv-zI9U5EN9KhNq5qYujqPctqYjj0kOrU0Y")