import discord
from discord import app_commands

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
async def self(interaction: discord.Interaction,primeiro_numero:float,tipo_de_operação:str, segundo_numero:float):
    if tipo_de_operação == "x":
        resultado = primeiro_numero*segundo_numero
        await interaction.response.send_message(f" a resposta é {resultado}")
    elif tipo_de_operação == "/":
        resultado = primeiro_numero/segundo_numero
        await interaction.response.send_message(f" a resposta é {resultado}") 
    elif tipo_de_operação == "-":
        resultado = primeiro_numero-segundo_numero
        await interaction.response.send_message(f" a resposta é {resultado}") 
    elif tipo_de_operação == "+":
        resultado = primeiro_numero+segundo_numero
        await interaction.response.send_message(f" a resposta é {resultado}") 

client.run('')