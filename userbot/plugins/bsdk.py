# gali plugin By LEGENDBOT
"""Emoji
Available Commands:
.bsdk"""

from telethon import events

import asyncio

from userbot import CMD_HELP
from userbot.utils import admin_cmd

@bot.on(admin_cmd("bsdk"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "gulli":
    await event.edit("galli")
    animation_chars = [
            "OK",
            "SUNN MADERCHOD",
            "TERI MAA KI CHUT PER RODE DAAL DUNGA",
            "BEHEN KE LUND",
            "TERI MAA KA DUD DABAKAR 500kg KA KAR DUNGQ",
            "MERA LAWDA LELE TU AGAR CHAIYE TOH",
            "GAANDU",
            "CHUTIYA",
            "TERI MAA KI CHUT PE JCB CHADHAA DUNGA",
            "SAMJHAA LAWDE",
            "YA DU TERE GAAND ME TAPAA TAP😂",
            "TERI BEHEN MERA ROZ LETI HAI",
            "TERI GF K SAATH MMS BANAA CHUKA HU🙈🤣🤣",
            "TU CHUTIYA TERA KHANDAANI CHUTIYA",
            "Yeahhhhhh",
            "AUR KITNA BOLU BEY MANN BHAR GAYA MERA🤣",
            "SALE BHEN KE LAWDE TERI BHEN KI CHUT PHARD DI MAINE JAKE DEKH LE BLACK HOLE BANA DIYA HU CHOD CHOD KE🤣",
            "Ab Nikal Ja Jaake Chkko K Saath Hilaa"
        ]

    for i in animation_ttl:
         
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])

CMD_HELP.update({
    "bsdk":"gali plugin h yrr use .bsdk"})
