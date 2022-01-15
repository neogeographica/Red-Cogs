"""IAm - Aliases for SelfRole add/remove commands."""
from .iam import IAm


def setup(bot):
    bot.add_cog(IAm())
