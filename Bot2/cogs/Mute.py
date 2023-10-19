import discord
from discord.ext import commands
import json


class Mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Mute.py is online.")

    @commands.command()
    @commands.has_permissions(manage_roles = True)  # permissions
    async def mute(self, ctx, user: discord.Member, *, role: discord.Role):
        if role.position > ctx.author.top_role.position:  # if the role is above users top role it sends error
            return await ctx.send('**:x: | That role is above your top role!**')
        if role in user.roles:
            await user.remove_roles(role)  # removes the role if user already has
            await ctx.send(f"Removed {role} from {user.mention}")
        else:
            await user.add_roles(role)  # adds role if not already has it
            await ctx.send(f"Added {role} to {user.mention}")


async def setup(client):
    await client.add_cog(Mute(client))
