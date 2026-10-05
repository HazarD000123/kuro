import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")
    
    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None): # the member: discord.Member tells discord.py to turn whatever the user typed (can be an id, mention, etc) into a Member object
                                                                # the = None makes the entire argument just optional
        member = member or ctx.author # return the mentioned user's avatar or your own avatar if none mentioned
        await ctx.send(member.display_avatar.url)
    
    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None): #repeating the same as above
        member = member or ctx.author
        # here we start using embeds to make our messages look cleaner and better
        embed = discord.Embed(title=f"{member.name}'s info", color=0x5865F2) # creating the embed structure with title and color
        embed.add_field(name="ID", value=member.id) # using a field to display the user's discord ID
        embed.add_field(name="Top Role", value=member.top_role)
        embed.add_field(name="Bot?", value=member.bot)
        embed.set_thumbnail(url=member.display_avatar.url) # displays the user's icon as a thumbnail on the embed
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Utility(bot))