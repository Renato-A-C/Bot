import discord
from discord.ext import commands
from datetime import timedelta

class moderarv2P(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def banir(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member} foi banido. Motivo: {reason}")

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def expulsar(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member} foi expulso. Motivo: {reason}")

    @commands.command(name="mute")
    @commands.has_permissions(moderate_members=True)
    async def castigar(self, ctx, member: discord.Member, duration: int, *, reason=None):
        until = discord.utils.utcnow() + timedelta(minutes=duration)
        await member.timeout(until, reason=reason)
        await ctx.send(f"{member} foi castigado por {duration} minutos. Motivo: {reason}")

    @commands.command(name="add_cargo")
    @commands.has_permissions(manage_roles=True)
    async def atribuir_cargo(self, ctx, member: discord.Member, role: discord.Role):
        print(f"{member} , {role}")
        await member.add_roles(role)
        await ctx.send(f"O cargo {role.name} foi atribuído a {member}.")

async def setup(bot):
    await bot.add_cog(moderarv2P(bot))
