import discord
from discord import app_commands
from discord.ext import commands
from datetime import timedelta

class moderarv2S(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="banir", description="Bane um membro do servidor.")
    @app_commands.checks.has_permissions(ban_members=True)
    async def banir(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        await member.ban(reason=reason)
        await interaction.response.send_message(f"{member} foi banido. Motivo: {reason}")

    @app_commands.command(name="expulsar", description="Expulsa um membro do servidor.")
    @app_commands.checks.has_permissions(kick_members=True)
    async def expulsar(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        await member.kick(reason=reason)
        await interaction.response.send_message(f"{member} foi expulso. Motivo: {reason}")

    @app_commands.command(name="castigar", description="Castiga um membro por um tempo determinado.")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def castigar(self, interaction: discord.Interaction, member: discord.Member, duration: int, reason: str = None):
        until = discord.utils.utcnow() + timedelta(minutes=duration)
        await member.timeout(until, reason=reason)
        await interaction.response.send_message(f"{member} foi castigado por {duration} minutos. Motivo: {reason}")

    @app_commands.command(name="atribuir_cargo", description="Atribui um cargo a um membro.")
    @app_commands.checks.has_permissions(manage_roles=True)
    async def atribuir_cargo(self, interaction: discord.Interaction, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await interaction.response.send_message(f"O cargo {role.name} foi atribuído a {member}.")

async def setup(bot):
    await bot.add_cog(moderarv2S(bot))
