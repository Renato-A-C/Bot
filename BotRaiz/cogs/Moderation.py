import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation.py is ready")
        
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, count: int):
        if count > 100:
            await ctx.send(embed=discord.Embed(color=discord.Color.red(), title="My limit is 100 messages"))
        elif count > 0:
            await ctx.channel.purge(limit=count + 1)  # `+1` includes the command message itself
            await ctx.send(f"No total, {count} messages were deleted", delete_after=5)  # Auto-delete the confirmation message after 5 seconds
        else:
            await ctx.send("Please provide a valid number greater than 0")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = "No reason provided"):
        await member.kick(reason=reason)
        
        conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Kicked:", value=f"{member.mention} has been kicked from the server by {ctx.author.mention}.", inline=False)
        conf_embed.add_field(name="Reason:", value=reason, inline=False)
        
        await ctx.send(embed=conf_embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason: str = "No reason provided"):
        await member.ban(reason=reason)
        
        conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Banned:", value=f"{member.mention} has been banned from the server by {ctx.author.mention}.", inline=False)
        conf_embed.add_field(name="Reason:", value=reason, inline=False)
        
        await ctx.send(embed=conf_embed)

    @commands.command(name="unban")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user_id: int):
        user = discord.Object(id=user_id)
        await ctx.guild.unban(user)
        
        conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Unbanned:", value=f"User with ID {user_id} has been unbanned from the server by {ctx.author.mention}.", inline=False)

        await ctx.send(embed=conf_embed)
        
async def setup(client):
    await client.add_cog(Moderation(client))