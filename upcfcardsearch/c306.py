import discord
from discord.ext import commands
from discord.utils import get

class c306(commands.Cog, name="c306"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Herald_of_the_Wasteland', aliases=['c306'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Herald of the Wasteland',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361261.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Banish up to 3 Rock monster from your Deck with the same Level; Special Summon 1 Rock monster from your Deck with the same Level as the banished monsters. During the next End Phase, return those 3 banished monsters to the GY. If this card is in your GY: You can banish this card from your GY, then target 1 Rock monster you control and 1 card your opponent controls; destroy them. You can only activate 1 effect of "Herald of the Wasteland" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c306(bot))