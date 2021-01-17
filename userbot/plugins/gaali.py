from userbot import *
from userbot.utils import *
from userbot.cmdhelp import CmdHelp
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="galli ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Abey O aatishbaji lodu")
        await asyncio.sleep(1)
        await event.edit("kaan khol ke sun lein")
        await asyncio.sleep(1)
        await event.edit("Baap ke samne Bakchodi nhi")
        await asyncio.sleep(1)
        await event.edit("Aur tera Baap Kaun h janta h na")
        await asyncio.sleep(1)
        await event.edit("Nhi janta to jaan le")
        await asyncio.sleep(1)
        await event.edit("Mai hu tera baap")
        await asyncio.sleep(1)
        await event.edit("Naam Roldex")
        await asyncio.sleep(1)
        await event.edit("**Roldex PAPA**")
        await asyncio.sleep(1)
        await event.edit("Abb Nikal yaha se madarchod")

@borg.on(events.NewMessage(pattern=r"\.baap", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Jaaa jakaar APNI maa se poochna `")
    await asyncio.sleep(0.9)
    await event.edit("WHO IS YOUR FATHER ?")
    await asyncio.sleep(0.9)
    await event.edit("PTA H TERI MAA KYA BOLEGI")
    await asyncio.sleep(0.9)
    await asyncio.edit("VO KHEGI LODEE BETA YE KOI POOCHNE KI BAAT HAI")
    await asyncio.sleep(0.9)
    await asyncio.edit("TERA BAAP ROLDEX HAI AUR VHI RHEGA")
    
    

@bot.on(admin_cmd(pattern=r"fuckyou$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"fuckyou$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 5
    animation_ttl = range(0, 21)
    animation_chars = [
        "`abe gandu,Ruk abhi teri gand marta hu lodu`",
        "`Dekh sale Teri gand me dal diya lund`",
        "`now twisting my lund in your gand`",
        "`Your Gand Fat giye Successfully`",
        "`es Gandu Ka Gand Fat gye a`",
        "`Gandu Asking again to taste my DICK🍌`",
        "`Requested accepted😻💋, Ready to taste my DICK🍌`",
        "`Getting again with fati hoi gand ready to fuck 👀`",
        "`You Gandu Is Ready To Fuck`",
        "`Fucking Your 😈😈\n\n\nYour  Ass Get Red\nTrying new SEX position to make u Squirt\n\nAlmost Done. 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your 😈😈\n\n\nYour Gand Get White\nu squirted like a shower💧💦👅\n\nAlmost Done..\n\nFucked Percentage... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your 😈😈\n\n\nYour gand Get Red\nDoing Extreme SEX with u👄\n\nAlmost Done...\n\nFucked Percentage... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your 😈😈\n\n\nYour gand Get Red\nWarming ur Ass🍑 to Fuck!🍑🍑\n\nAlmost Done....\n\nFucked Percentage... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your 😈😈\n\n\nYour ASS🍑 Get Red\nInserted my Penis🍌 in ur ASS🍑\n\nAlmost Done.....\n\nFucked Percentage... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your 😈😈\n\n\nYour ASS🍑 Get Red\ndoing extreme sex with u\n\nAlmost Done......\n\nFucked Percentage... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your 😈😈\n\n\nYour Boobs🤚😘 are Awesome\nPressing u tight Nipples🤚👀\n\nAlmost Done.......\n\nFucked Percentage... 84%\n███████████████████▒▒▒▒▒▒ `",
        "`Fucking Your 😈😈\n\n\nYour Gand Get Horny\nDoing Gandsex with you👄💋\n\nAlmost Done........\n\nFucked Percentage... 89%\n██████████████████████▒▒▒ `",
        "`Fucking Your 😈😈\n\n\nYour Boobs🤚😘 are Awesome\nI am getting ready to cum in ur Mouth👄\n\nAlmost Done.......\n\nFucked Percentage... 90%\n██████████████████████▒▒▒ `",
        "`Fucking Your 😈😈\n\n\nYour  Boobs🤚😘 are Awesome\nFinally, I have cummed in ur Mouth👅👄\n\nAlmost Done.......\n\nFucked Percentage... 96%\n████████████████████████▒ `",
        "`Fucking Your 😈😈\n\n\nYour ur Gand is Awesome\nyou is Licking my Dick🍌 in the Awesome Way✊🤛🤛👅👄\n\nAlmost Done.......\n\nFucked Percentage... 100%\n█████████████████████████ `",
        "`Fucking Your 😈😈\n\n\nYour  ASS🍑 Get Red\nCummed On ur Mouth👅👄\n\nYou got Pleasure\n\nResult: Now I Have 1 More SEX Partner 👍👍 abh ja ki kise aur se chuda gandu`",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 21])


