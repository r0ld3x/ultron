import random
import re
import time

import requests
from cowpy import cow
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply



@bot.on(admin_cmd(pattern=f"repo", outgoing=True))
@bot.on(sudo_cmd(pattern=f"repo", allow_sudo=True))
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await edit_or_reply(e, "Click [here](https://github.com/r0ld3x/ultron) to open this __Ultron__ Repo.. Join channel :- @rifelmods")


@bot.on(admin_cmd(pattern="rpt(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="rpt(?: |$)(.*)", allow_sudo=True))
async def stretch(stret):
    """ Stretch it."""
    if not stret.text[0].isalpha() and stret.text[0] not in ("/", "#", "@", "!"):
        textx = await stret.get_reply_message()
        message = stret.text
        message = stret.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await edit_or_reply(stret, "`GiiiiiiiB sooooooomeeeeeee teeeeeeext!`")
            return

        count = random.randint(3, 10)
        reply_text = re.sub(
            r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])", (r"\1" * count), message
        )
        await edit_or_reply(stret, reply_text)
