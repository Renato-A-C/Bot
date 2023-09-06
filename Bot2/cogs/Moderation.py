import discord
from discord.ext import commands, tasks
import random
import os
import asyncio
from itertools import cycle

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderaçao.py is ready")
        
    @commands.command()
    @commands.has_permissions(manage_messages= True)
    async def clear(self,ctx, count: int):
        if (count >100):
            await ctx.send(embed = discord.Embed(color=discord.Color.red(), title=f"My limit is 100 message"))
        if (count<=100) and (count>0):
            await ctx.channel.purge(limit=count+1)
            await ctx.send(f"No total, {count} mensagens foram apagadas")
        else:
            await ctx.send(f"Primeiro coloque um número válido")
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self,ctx,member: discord.Member, modreason):
        await ctx.guild.kick(member)
        
        conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Kicked:", value=f"{member.mention} has been kicked from the server by {ctx.author.mention}.", inline=False)
        conf_embed.add_field(name="Reason:", value=modreason,inline=False)
        
        await ctx.send(embed=conf_embed)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self,ctx,member: discord.Member, modreason):
        await ctx.guild.ban(member)
        
        conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="banned:", value=f"{member.mention} has been banned from the server by {ctx.author.mention}.", inline=False)
        conf_embed.add_field(name="Reason:", value=modreason,inline=False)
        
        await ctx.send(embed=conf_embed)

    @commands.command(name="unban")
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, userId):
        user = discord.Object(id=userId)
        await ctx.guild.unban(user)
        
        conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="unbaned:", value=f"@<{user.mention}> has been unbanned from the server by {ctx.author.mention}.", inline=False)


        await ctx.send(embed=conf_embed)
        
        @clear.error
        async def clear_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("Error: Falta algum tipo de parâmetro, ou tá excedendo, é um argumento e é em numero")
async def setup(client):
    await client.add_cog(Moderation(client))
    