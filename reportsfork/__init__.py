from redbot.core.bot import Red
from .reportsfork import ReportsFork


async def setup(bot: Red) -> None:
    await bot.add_cog(ReportsFork(bot))
