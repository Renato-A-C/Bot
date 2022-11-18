<<<<<<< HEAD
import discord
from discord import app_commands

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id=658508846167359488))
            self.synced = True
        print(f"Entramos como {self.user}.")
        
client = aclient()
tree = app_commands.CommandTree(client)

@tree.coomand(name= "test", description = "testing", guild = discord.Object(id = 658508846167359488))
async def self(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f"Hello {name}! I was made with Discord. py")
    
client.run('MTA0MzAxMTY2Mzc0MzQyNjYyMg.G6B8OK.-FjTUNaB_Xy_YbARdBjOo_W9tMgq1hYiz7_0nU')