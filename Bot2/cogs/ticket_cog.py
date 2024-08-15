import discord
from discord.ext import commands
from discord.ui import Button, View

class TicketView(View):
    def __init__(self, *, channel: discord.TextChannel):
        super().__init__(timeout=None)
        self.channel = channel

    @discord.ui.button(label="Fechar Ticket", style=discord.ButtonStyle.red)
    async def close_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.guild_permissions.manage_channels:
            await self.channel.delete()
        else:
            await interaction.response.send_message("Você não tem permissão para fechar este ticket.", ephemeral=True)

class TicketCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ticket')
    async def create_ticket(self, ctx):
        guild = ctx.guild
        category = discord.utils.get(guild.categories, name="Tickets")
        if category is None:
            category = await guild.create_category(name="Tickets")

        ticket_channel = await guild.create_text_channel(
            name=f"ticket-{ctx.author.name}",
            category=category
        )

        view = TicketView(channel=ticket_channel)
        await ticket_channel.send(f"Ticket criado por {ctx.author.mention}.", view=view)

        await ctx.send(f"Ticket criado: {ticket_channel.mention}")

    @commands.command(name='ticketpanel')
    async def ticket_panel(self, ctx):
        button = Button(label="Abrir Ticket", style=discord.ButtonStyle.green)

        async def button_callback(interaction: discord.Interaction):
            guild = interaction.guild
            category = discord.utils.get(guild.categories, name="Tickets")
            if category is None:
                category = await guild.create_category(name="Tickets")

            ticket_channel = await guild.create_text_channel(
                name=f"ticket-{interaction.user.name}",
                category=category
            )

            view = TicketView(channel=ticket_channel)
            await ticket_channel.send(f"Ticket criado por {interaction.user.mention}.", view=view)

            await interaction.response.send_message(f"Ticket criado: {ticket_channel.mention}", ephemeral=True)

        button.callback = button_callback

        view = View()
        view.add_item(button)

        await ctx.send("Clique no botão abaixo para abrir um ticket:", view=view)

async def setup(bot):
    await bot.add_cog(TicketCog(bot))
