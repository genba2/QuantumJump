import asyncio
from datetime import datetime

from lib.cog import Cog
from lib.command import Command, makeCommand
from lib.styling import Styles
from lib.util import get_current_sha1, get_latest_sha1


class Builtins(Cog):
    @makeCommand(aliases=["version"], description="get the current version")
    async def version(self, c: Command):
        message = ":crystal_ball: currently using: *{}* | Latest is: *{}*".format(
            get_current_sha1(),
            await get_latest_sha1()
        )
        await self.send_message(message)

    @makeCommand(aliases=["uptime"], description="get the bot's uptime")
    async def uptime(self, c: Command):
        current = datetime.now()
        start = datetime.fromtimestamp(self.bot.start_time)
        difference = str(current - start)
        # strip after the decimal
        message = "has been alive for {} :stopwatch:".format(
            str(difference)[:7].replace(":", ";"))
        await self.send_action(message, style=Styles.bold)

    @makeCommand(aliases=["timer"], description="a seconds timer ")
    async def timer(self, c: Command):
        if c.message.isdigit():
            await self.send_message(f"Set a timer set for {c.message}")
            await asyncio.sleep(int(c.message))
            await self.send_message(f"Timer has expired!")
