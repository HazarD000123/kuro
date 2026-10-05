import discord
from discord.ext import commands

@commands.Cog.listener()
async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance (error, commands.MissingRequiredArgument):
        await ctx.send(f"You are missing: `{error.param.name}")
        return
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("I was not able to find that member")
        return
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permissions to do that!")
        return
    raise error