import discord

import time
import datetime
import math
from discord import app_commands
from discord.ext import commands
import random

#z0n4 571722603920752650 guild = discord.Object(id=571722603920752650
#ads 1042560674812923914
class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await zonbot.sync()
            self.synced = True
        print(f"Entramos como {self.user}.")
        
client = abot()
zonbot = app_commands.CommandTree(client)
@zonbot.command(name= "teste", description = "testando",)
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"Olá! eu fui feito a base do Discord.py . Sim eu tô funcionando :thumbsup:") 
@zonbot.event
async def on_message():
    print("ready")



@zonbot.command(name= "lapadaseca", description = "eita bixo")
async def self(interaction: discord.Interaction):
    a="https://tenor.com/view/toma-pra-respeitar-paulo-wilson-gif-18861036"
    await interaction.response.send_message(f"TOME\n {a}")

@zonbot.command(name= "pergunte", description = "e o bot responde")
async def self(interaction: discord.Interaction, pergunta: str):
    respostas= ["não sei", "quem sabe","se eu soubesse eu te falava","não :)","a va ti lascar rapa","Sim","para com issae bicho","IMPOSSÍVEL","só tem um jeito: capotando na porrada","olha o dicionário q tu descobre","se vc n sabe imagina eu","...","em resumo da ópera: BUGUEI", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi hendrerit ex vitae molestie aliquet. Proin a elit accumsan, lobortis urna ut, consectetur erat. Nam ut est mattis, porta mauris vel, suscipit orci. Curabitur at imperdiet diam. Fusce sed maximus arcu. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur accumsan gravida sagittis. Curabitur ullamcorper diam eu placerat convallis. Proin imperdiet bibendum metus, ultrices consectetur ante luctus eu. Phasellus quis elit purus. Donec orci leo, rhoncus sit amet nibh eu, accumsan efficitur justo. Quisque eu justo porta dui lobortis consequat eu non purus. Aenean facilisis non lacus ut fringilla. Sed libero risus, viverra in viverra in, feugiat nec quam. Maecenas imperdiet sollicitudin quam vitae scelerisque.Phasellus vel dui in nulla laoreet dictum sed id erat. Quisque sollicitudin est nec velit ultricies, eget commodo augue euismod. Sed euismod vulputate turpis. Donec magna risus, tincidunt et enim vitae, vehicula dictum augue. Vivamus feugiat diam a velit imperdiet sagittis. Etiam ut nibh venenatis, vestibulum nisl quis, ornare nisl. Mauris vel eros quis mauris bibendum interdum sed nec lorem."]
    await interaction.response.send_message(f"**Pergunta: **{pergunta}\n**Resposta**: {random.choice(respostas)}")   

@zonbot.command(name="randomfoto",description="acha uma foto ae")
async def get_random_image(img):
    
    num= random.randint(144, 1920)   
    num2= random.randint(144, 1920) 

    Embed = discord.Embed(
        title="Foto buscada com sucesso",
        description=f"Lembrando q é random msm",
        color=discord.Color.random(),
        
        )
    Embed.set_image(url=(f"https://picsum.photos/{num}/{num2}"))
    await img.channel.send(embed=Embed)
@zonbot.command(name="fotorandom",description="acha uma foto ae")
async def FotoRandom(img):
    
    num= random.randint(144, 1920)   
    num2= random.randint(144, 1920) 

    await img.response.send_message(f"https://picsum.photos/{num}/{num2}")
@zonbot.command(name= "surra", description = "em alguém")
async def self(interaction: discord.Interaction, atacante: str, atacado: str, objeto:str, tempo:float):
    if type(tempo) != float:
        await interaction.response.send_message(f"comando errado, o tempo deve ser apenas numérico")
    else:
        await interaction.response.send_message(f"Por pedido de {atacante}, o alvo {atacado} vai levar uma surra de {objeto} por {round(tempo)} minutos")
    

@zonbot.command(name="calculadora", description="calcula algo")
@app_commands.describe(operacoes='tipos de operações')
@app_commands.choices(operacoes=[
    discord.app_commands.Choice(name='vezes',value=1),
    discord.app_commands.Choice(name='divisao',value=2),
    discord.app_commands.Choice(name='subtraçao',value=3),
    discord.app_commands.Choice(name='adiçao',value=4),
    #discord.app_commands.Choice(name='porcentagem',value=5)
])
async def self(interaction: discord.Interaction,primeiro_numero:float,operacoes:discord.app_commands.Choice[int], segundo_numero:float):
    
    if operacoes.name == "vezes":
        resultado = primeiro_numero*segundo_numero
        #@app_commands.describe(operacoes='= {}'.format(str(num)))
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
@zonbot.command(name= "fotocj", description = "Foto do Cejota",)
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"https://c1.wallpaperflare.com/preview/240/187/733/carbon-black-barbecue-charcoal.jpg") 
@zonbot.command(name= "devat", description = "link na descrição",)
async def self(interaction: discord.Interaction):
    await interaction.response.send_message("https://discord.com/developers/active-developer") 

client.run("MTA0MzAxMTY2Mzc0MzQyNjYyMg.GUADCe.Axu9ziWGTWKZidyxGJ9U2VFOB1p254LbHcO__Y")