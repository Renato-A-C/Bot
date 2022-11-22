import discord
from discord import app_commands

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id=571722603920752650))
            self.synced = True
        print(f"Entramos como {self.user}.")
        
client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name= "test", description = "testing", guild = discord.Object(id = 571722603920752650))
async def self(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f"Olá {name}! eu fui feito a base do Discord.py")   
     
@tree.command(name= "surra", description = "em alguém", guild = discord.Object(id = 571722603920752650))
async def self(interaction: discord.Interaction, atacante: str, atacado: str, objeto:str, tempo:str):
    await interaction.response.send_message(f"Por pedido de {atacante}, o alvo {atacado} vai levar uma surra de {objeto} por {tempo} minutos")
    
@client.event
async def on_ready():
    print('calculadora')
    DiscordComponents(client)

buttons = [Button(style=ButtonStyle.grey, Label='1')]
    
    
client.run('MTA0MzAxMTY2Mzc0MzQyNjYyMg.GgvdSC.Pd0BM0mq4UH_VXl48dUd9HDYe3b77vkrxqkPI0')