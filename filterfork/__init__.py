from .filterfork import FilterFork
from redbot.core.bot import Red


async def setup(bot: Red) -> None:
    cog = FilterFork(bot)
    await cog.initialize()
    bot.add_cog(cog)
