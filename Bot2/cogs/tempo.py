import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta, timezone
import asyncio

class Tempo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.repeat_task.start()  # Inicia a tarefa quando a Cog é carregada

    @commands.Cog.listener()
    async def on_ready(self):
        print("Tempo funcional")

    @tasks.loop(hours=24)
    async def repeat_task(self):
        today = datetime.now(timezone.utc).weekday()
        if today == 4:  # Quinta-feira
            channel = self.bot.get_channel(1206390098514546729)
            await channel.send("# Hoje é quinta-feira! https://cdn.discordapp.com/attachments/1272065177197477969/1273042710701277235/Engineer_TF2_sings_Out_of_Touch.mp4?ex=66c272ea&is=66c1216a&hm=ac3814e3d408fd8798f58e6c4d6c87519b37b33297740bd344815fb8131e8b43&")

    @repeat_task.before_loop
    async def before_repeat_task(self):
        await self.bot.wait_until_ready()
        now = datetime.now(timezone.utc)
        next_run = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        sleep_duration = (next_run - now).total_seconds()
        await asyncio.sleep(sleep_duration)
async def setup(bot):
    await bot.add_cog(Tempo(bot))