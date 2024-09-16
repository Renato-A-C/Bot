import discord
import random
from discord.ext import commands
from discord import app_commands

class ticketSlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    
    
    
    discord.app_commands.command(name="ticket", description="Cria um ticket de suporte.")
    async def ticket(self, interaction: discord.Interaction):
        embed_message = self.create_embed(
            title="Ticket de Suporte",
            description="Clique no botão abaixo para criar um canal de suporte.",
            interaction=interaction
        )
        button = discord.ui.Button(label="Criar Ticket", style=discord.ButtonStyle.green)

        async def button_callback(interaction):
            # Lógica para criar o canal de suporte aqui
            await interaction.response.send_message("Canal de suporte criado!", ephemeral=True)
        
        button.callback = button_callback

        view = discord.ui.View()
        view.add_item(button)

        await interaction.response.send_message(embed=embed_message, view=view)
        
async def setup(bot):
    await bot.add_cog(ticketSlash(bot))