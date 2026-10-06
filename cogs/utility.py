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
    async def avatar(self, ctx, member: discord.User = None): # the member: discord.Member tells discord.py to turn whatever the user typed (can be an id, mention, etc) into a Member object
                                                                # the = None makes the entire argument just optional
        # return the mentioned user's avatar or your own avatar if noone mentioned
        if user == None:
            user = ctx.author
        
        user = await self.bot.fetch_user(user.id)
        
        embed= discord.Embed(title=f"{member.name}'s pfp", color=0xFFFFFF)
        embed.set_image(url=member.display_avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command(help="Show someone's banner")
    async def banner(self, ctx, user: discord.User = None):
        if user == None:
            user = ctx.author # if no person is mentioned then it returns to the person who ran it
        
        user = await self.bot.fetch_user(user.id) # fetches their id from discord api
        
        if user.banner == None:
            await ctx.send(f"{user.name} **has no** banner set!") # if they have no banner send this message
        else:
            embed = discord.Embed(title=f"{user.name}'s banner", color=0xFFFFFF)
            embed.set_image(url=user.banner.url)
            await ctx.send(embed=embed)
    
    @commands.command(aliases=["ui", "uinfo", "whois"], help="Show info of someone")
    async def userinfo(self, ctx, member: discord.Member = None): #repeating the same as above
        if member == None:
            member = ctx.author
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
        
        embed.set_thumbnail(url=member.display_avatar.url) # thumbnail avatar
        
        if not ctx.guild.chunked:
            await ctx.guild.chunk()
        
        members= sorted(ctx.guild.members, key=lambda m: m.joined_at or discord.utils.utcnow())
        position = members.index(member) + 1
        embed.set_footer(text=f"Join Position: {position} · {len(member.mutual_guilds)} mutual servers")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def serverinfo(self, ctx):
        guild=ctx.guild
        
        embed= discord.Embed(title=f"{guild.name} ({guild.id})")
        embed.add_field(name="**Server owner**", value=guild.owner)
        embed.add_field(name="**Members**", value=guild.member_count)
        embed.add_field(name="**Roles**", value=len(guild.roles))
        embed.add_field(name="**Channels**", value=len(guild.channels))
        embed.add_field(name="**Emojis**", value=len(guild.emojis))
        embed.add_field(name="**Verification**", value=guild.verification_level)
        embed.add_field(name="**Boosts**", value=guild.premium_subscription_count)
        
        await ctx.send(embed=embed)
        
        


async def setup(bot):
    await bot.add_cog(Utility(bot))