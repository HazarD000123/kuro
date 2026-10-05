import discord
from discord.ext import commands
import math
import datetime

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    
    @commands.command()
    async def ping(self, ctx):
        latency = self.bot.latency
        embed= discord.Embed(description=f"{ctx.author.mention}: kuro's ping is `{round(latency*1000)}` ms", color=0xFFFFFF)
        await ctx.send(embed=embed)
    
    @commands.command(aliases=["av", "pfp"], help="Show someone's pfp")
    async def avatar(self, ctx, member: discord.Member = None): # the member: discord.Member tells discord.py to turn whatever the user typed (can be an id, mention, etc) into a Member object
                                                                # the = None makes the entire argument just optional
        member = member or ctx.author # return the mentioned user's avatar or your own avatar if none mentioned
        embed= discord.Embed(title=f"{member.name}'s pfp", color=0xFFFFFF)
        embed.set_image(url=member.display_avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command(aliases=["ui", "uinfo", "whois"], help="Show userinfo of someone")
    async def userinfo(self, ctx, member: discord.Member = None): #repeating the same as above
        member = member or ctx.author
        # here we start using embeds to make our messages look cleaner and better
        embed = discord.Embed(title=f"{member.name} ({member.id})", color=0xFFFFFF) # creating the embed structure with title and color
        created=member.created_at
        joined = member.joined_at
        
        embed.add_field(name="**Dates**", value=(
            f"**Created**: {discord.utils.format_dt(created, 'f')} ({discord.utils.format_dt(created, 'R')})\n" # uses discord's time formatting
            f"**Joined**: {discord.utils.format_dt(joined, 'f')} ({discord.utils.format_dt(joined, 'R')})"
        ),
        inline=False,
    )
        roles = [role.mention for role in reversed(member.roles) if role != ctx.guild.default_role] # shows roles from highest order first and ignores @everyone role
        embed.add_field(name=f"**Roles** ({(len(member.roles))-1})", value="".join(roles or "none"), inline=False) # showing member roles while ignoring @everyone role
        
        embed.set_thumbnail(url=member.avatar.url) # thumbnail avatar
        
        if not ctx.guild.chunked:
            await ctx.guild.chunk()
        
        members= sorted(ctx.guild.members, key=lambda m: m.joined_at or discord.utils.utcnow())
        position = members.index(member) + 1
        embed.set_footer(text=f"Join Position: {position}"+f"{len(member.mutual_guilds)} mutual servers")
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Utility(bot))