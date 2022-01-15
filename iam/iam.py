"""Module for the IAm cog."""
import discord
from redbot.core import commands


class SelfRole(commands.Converter):
    """Same converter as the one used in Admin, except it grabs the cog differently."""

    async def convert(self, ctx: commands.Context, arg: str) -> discord.Role:
        """Convert an arg to a SelfRole."""
        admin = ctx.bot.get_cog("Admin")
        if admin is None:
            raise commands.BadArgument("Admin is not loaded.")

        selfroles = await admin.config.guild(ctx.guild).selfroles()

        role_converter = commands.RoleConverter()
        role = await role_converter.convert(ctx, arg)

        if role.id not in selfroles:
            raise commands.BadArgument("The provided role is not a valid selfrole.")
        return role


class IAm(getattr(commands, "Cog", object)):
    """IAm - Aliases for selfrole add and remove."""

    @commands.command()
    async def iam(self, ctx: commands.Context, *, role: SelfRole):
        """Alias for selfrole add."""
        admin_cog = ctx.bot.get_cog("Admin")
        if admin_cog is None:
            await ctx.send("The `admin` cog must be loaded to use this command.")
            return
        await ctx.invoke(admin_cog.selfrole_add, selfrole=role)

    @commands.command()
    async def iamnot(self, ctx: commands.Context, *, role: SelfRole):
        """Alias for selfrole remove."""
        admin_cog = ctx.bot.get_cog("Admin")
        if admin_cog is None:
            await ctx.send("The `admin` cog must be loaded to use this command.")
            return
        await ctx.invoke(admin_cog.selfrole_remove, selfrole=role)
