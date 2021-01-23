from userbot import *
from userbot.utils import *
from userbot.cmdhelp import CmdHelp
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ultron"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

PM_IMG = "https://telegra.ph/file/2f0a575332c180d75e7b5.png"
pm_caption = f"🔅 🔅 🔅HEY I AM [ULTRON](https://t.me/rifelmods) PRIME🔅 🔅 🔅 THE PRIVATE ASSISTANT OF MY MASTER [{DEFAULTUSER}](tg://user?id={kraken}) \n\n"

pm_caption += "MY TELETHON VERSION: 1.15.0 \n"

pm_caption += "MY PYTHON VERSION: 3.7.4 \n"

pm_caption += f"DEVLOPED BY:  [ROLDEX](https://t.me/r0ld3x)\n"

pm_caption += "SUPPORT CHANNEL : [HERE](https://t.me/rifelmods)\n"

pm_caption += "SUPPORT GROUP : [HERE](https://t.me/rifelmodschats)\n"

pm_caption += "[✨REPO✨](https://github.com/r0ld3x/ultron) 🔹 [📜License📜](https://github.com/r0ld3x/ultron/blob/master/LICENSE)\n\n"



@bot.on(admin_cmd(outgoing=True, pattern="ultron$"))
@bot.on(sudo_cmd(pattern="ultron$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    """ For .ultron command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()

CmdHelp("ultron").add_command(
  'ultron', None, 'Check Who Is Ultron'
).add()
