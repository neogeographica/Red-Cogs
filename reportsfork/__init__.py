from redbot.core.bot import Red
from .reportsfork import ReportsFork


def setup(bot: Red):
    bot.add_cog(ReportsFork(bot))
