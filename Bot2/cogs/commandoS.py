import discord
import random
from discord.ext import commands
from discord import app_commands

class commandoS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Slashs operacionais.")

    @app_commands.command(name="teste", description="testando")
    async def teste(self, interaction: discord.Interaction):
        await interaction.response.send_message("Olá! Eu fui feito a base do Discord.py. Sim, eu tô funcionando :thumbsup:")

    @app_commands.command(name="lapadaseca", description="eita bixo")
    async def lapadaseca(self, interaction: discord.Interaction):
        gif_url = "https://tenor.com/view/toma-pra-respeitar-paulo-wilson-gif-18861036"
        await interaction.response.send_message(f"TOME\n {gif_url}")

    @app_commands.command(name="pergunte", description="E o bot responde")
    async def pergunte(self, interaction: discord.Interaction, pergunta: str):
        try:
            with open("Bot/Bot2/cogs/quack/anwers.txt", "r") as f:
                respostas_random = f.readlines()
            # Remove a quebra de linha das respostas, caso existam
            respostas_random = [resposta.strip() for resposta in respostas_random]
            resposta = random.choice(respostas_random)
            await interaction.response.send_message(f"**Pergunta:** {pergunta}\n**Resposta:** {resposta}")
        except FileNotFoundError:
            await interaction.response.send_message("Não consegui encontrar o arquivo com as respostas.")
        except Exception as e:
            await interaction.response.send_message(f"Ocorreu um erro: {str(e)}")

    @app_commands.command(name="randomfoto", description="acha uma foto aleatória")
    async def randomfoto(self, interaction: discord.Interaction):
        num = random.randint(144, 1920)
        num2 = random.randint(144, 1920)
        embed = discord.Embed(
            title="Foto buscada com sucesso",
            description="Lembrando que é random mesmo",
            color=discord.Color.random(),
        )
        embed.set_image(url=f"https://picsum.photos/{num}/{num2}")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="fotorandom", description="acha uma foto aleatória")
    async def fotorandom(self, interaction: discord.Interaction):
        num = random.randint(144, 1920)
        num2 = random.randint(144, 1920)
        await interaction.response.send_message(f"https://picsum.photos/{num}/{num2}")

    @app_commands.command(name="fotocj", description="Foto do Cejota")
    async def fotocj(self, interaction: discord.Interaction):
        await interaction.response.send_message("https://c1.wallpaperflare.com/preview/240/187/733/carbon-black-barbecue-charcoal.jpg")

    @app_commands.command(name="surra", description="em alguém")
    async def surra(self, interaction: discord.Interaction, atacante: str, atacado: str, objeto: str, tempo: float):
        if not isinstance(tempo, float):
            await interaction.response.send_message("Comando errado, o tempo deve ser apenas numérico")
        else:
            
            await interaction.response.send_message(
                f"Por pedido de {atacante}, o alvo {atacado} vai levar uma surra de {objeto} por {round(tempo)} minutos"
            )

    @app_commands.command(name="calculadora", description="calcula algo")
    @app_commands.describe(operacoes='tipos de operações')
    @app_commands.choices(operacoes=[
        discord.app_commands.Choice(name='vezes', value=1),
        discord.app_commands.Choice(name='divisao', value=2),
        discord.app_commands.Choice(name='subtração', value=3),
        discord.app_commands.Choice(name='adição', value=4),
    ])
    async def calculadora(self, interaction: discord.Interaction, primeiro_numero: float, operacoes: discord.app_commands.Choice[int], segundo_numero: float):
        if operacoes.name == "vezes":
            resultado = primeiro_numero * segundo_numero
        elif operacoes.name == "divisao":
            resultado = primeiro_numero / segundo_numero
        elif operacoes.name == "subtração":
            resultado = primeiro_numero - segundo_numero
        elif operacoes.name == "adição":
            resultado = primeiro_numero + segundo_numero
        await interaction.response.send_message(f"A resposta é {resultado}")

    @app_commands.command(name="devat", description="link na descrição")
    async def devat(self, interaction: discord.Interaction):
        await interaction.response.send_message("https://discord.com/developers/active-developer")

    async def cog_load(self):
        await self.bot.tree.sync()

async def setup(bot):
    await bot.add_cog(commandoS(bot))
