

import os
from datetime import datetime

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file

from userbot import ALIVE_NAME
from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp
import io
import os

from userbot import *
from userbot.utils import *
from userbot.plugins.sql_helper.broadcast_sql import (
    add_chnnl_in_db,
    already_added,
    get_all_chnnl,
    rm_channel,
)
from userbot.utils import admin_cmd



@bot.on(admin_cmd(pattern="badd ?(.*)"))
async def _(event):
    input_chnnl = event.pattern_match.group(1)
    sed = 0
    oks = 0
    if input_chnnl == "all":
        await event.edit("`Adding All Channel TO DB.`")
        addall = [
            d.entity
            for d in await event.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in addall:
            try:
                if i.broadcast:
                    if i.creator or i.admin_rights:
                        if already_added(i.id):
                            oks += 1
                        else:
                            add_chnnl_in_db(i.id)
                            sed += 1
            except BaseException:
                pass
        await event.edit(
            f"Process Completed. Added {sed} Channel To List. Failed {oks} Due to already Added !"
        )
        return
    elif input_chnnl == "":
        if event.is_channel and event.is_group:
            input_chnnl = event.chat_id
        else:
            await event.edit("Please Give Group / Channel ID !")
            return
    if already_added(input_chnnl):
        await event.edit("This Channel Already Found in Database.")
        return
    if not already_added(input_chnnl):
        add_chnnl_in_db(input_chnnl)
        await event.edit(f"Fine. I have Added {input_chnnl} To DataBase.")
        await borg.send_message(Config.PRIVATE_GROUP_ID, f"Added {input_chnnl} To DB")


@bot.on(admin_cmd(pattern="brm ?(.*)"))
async def _(event):
    input_chnnl = event.pattern_match.group(1)
    all_chnnl = get_all_chnnl()
    if input_chnnl == "all":
        for channelz in all_chnnl:
            rm_channel(channelz.chat_id)
        await event.edit("Fine. Cleared All Channel Database")
        return
    if input_chnnl is "":
        if event.is_channel and event.is_group:
            input_chnnl = event.chat_id
        else:
            await event.edit("Please Give Group / Channel ID")
            return
    if already_added(input_chnnl):
        rm_channel(input_chnnl)
        await event.edit(f"Fine. I have Removed {input_chnnl} From DataBase.")
        await borg.send_message(Config.PRIVATE_GROUP_ID, f"Removed {input_chnnl} From DB")
    elif not already_added(input_chnnl):
        await event.edit(
            "Are You Sure? , You Haven't Added This Group / Channel To Database"
        )


@bot.on(admin_cmd(pattern="broadcast"))
async def _(event):
    await event.edit("**Fine. Broadcasting in Progress. Kindly Wait !**")
    sedpath = Config.TMP_DOWNLOAD_DIRECTORY
    all_chnnl = get_all_chnnl()
    if len(all_chnnl) == 0:
        await event.edit("No Channel Or Group Found On Database. Please Check Again")
        return
    total_errors = 0
    total_count = 0
    errorno = ""
    total_chnnl = len(all_chnnl)
    if event.reply_to_msg_id:
        hmm = await event.get_reply_message()
    else:
        event.edit("Reply To Some Message.")
        return
    if hmm and hmm.media:
        ok = await borg.download_media(hmm.media, sedpath)
        for channelz in all_chnnl:
            try:
                await borg.send_file(int(channelz.chat_id), file=ok, caption=hmm.text)
                total_count += 1
            except Exception as e:
                total_errors += 1
                errorno += f"{e} \n"
        await borg.send_message(
            Config.PRIVATE_GROUP_ID,
            f"Error : {total_errors}\nError : {errorno} \n\n",
        )
        if os.path.exists(ok):
            os.remove(ok)
    elif hmm and hmm.text:
        for channelz in all_chnnl:
            try:
                await borg.send_message(int(channelz.chat_id), hmm.text)
                total_count += 1
            except Exception as e:
                total_errors += 1
    elif hmm.message.poll:
        await event.edit("Bruh, This Can't Be Broadcasted.")
        return
    await event.edit(
        f"BroadCast Success In : {total_count} \nFailed In : {total_errors} \nTotal Channel In DB : {total_chnnl}"
    )
    await borg.send_message(
        Config.PRIVATE_GROUP_ID,
        f"BroadCast Success In : {total_count} \nFailed In : {total_errors} \nTotal Channel In DB : {total_chnnl}",
    )


@bot.on(admin_cmd(pattern="bforward"))
async def _(event):
    all_chnnl = get_all_chnnl()
    if len(all_chnnl) == 0:
        await event.edit("No Channel Or Group Found On Database. Please Check Again")
        return
    total_errors = 0
    total_count = 0
    errorno = ""
    total_chnnl = len(all_chnnl)
    if event.reply_to_msg_id:
        hmm = await event.get_reply_message()
    else:
        event.edit("Reply To Some Message.")
        return
    try:
        for forbard in all_chnnl:
            await hmm.forward_to(forbard.chat_id)
            total_count += 1
    except Exception as e:
        total_errors += 1
        errorno += f"{e} \n"
    await borg.send_message(
        Config.PRIVATE_GROUP_ID,
        f"Failed in {forbard.chat_id} Because Of Error : `{errorno}` \n\n",
    )
    await event.edit(
        f"Forward Success in {total_count} And Failed In {total_errors} And Total Channel In Db is {total_chnnl}"
    )
    await borg.send_message(
        Config.PRIVATE_GROUP_ID,
        f"Forward Success in {total_count} And Failed In {total_errors} And Total Channel In Db is {total_chnnl}",
    )


@bot.on(admin_cmd(pattern="bstat"))
async def _(event):
    total_chnnl = get_all_chnnl()
    chnnl_list = ""
    for starked in total_chnnl:
        try:
            chnnl_list += ("==> {} \n").format(starked.chat_id)
        except Exception:
            pass
    with io.BytesIO(str.encode(chnnl_list)) as tedt_file:
        tedt_file.name = "dbchnnllist.txt"
        await borg.send_file(
            event.chat_id,
            tedt_file,
            force_document=True,
            caption="Total Channel In DB.",
            allow_cache=False,
        )
CmdHelp("broadcast").add_command(
  'badd', 'channel_id', 'Adds the given channel/group to database.'
  ).add_command(
  'badd all', None, 'Adds all the channel/groups to database where you are admin.'
).add_command(
  'brm', 'channel_id', 'Removes the Specified Channel From database.'
).add_command(
  'broadcast', 'Reply-To-Msg', 'Broadcasts To All Channel in DB, Even Supports Media'
).add_command(
  'bstat', None, 'Shows list of channels/groups in database.'
).add()

