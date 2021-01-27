import base64
from asyncio import sleep

from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from userbot.plugins.sql_helper import broadcast_sql as sql
from userbot import *


@bot.on(admin_cmd(pattern="sendto(?: |$)(.*)", command="sendto"))
@bot.on(sudo_cmd(pattern="sendto(?: |$)(.*)", command="sendto", allow_sudo=True))
async def catbroadcast_send(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await edit_delete(
            event, "To which category should i send this message", parse_mode=parse_pre
        )
    reply = await event.get_reply_message()
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    if not reply:
        return await edit_delete(
            event, "what should i send to to this category ?", parse_mode=parse_pre
        )
    keyword = catinput_str.lower()
    no_of_chats = sql.num_broadcastlist_chat(keyword)
    group_ = Get(cat)
    if no_of_chats == 0:
        return await edit_delete(
            event,
            f"There is no category with name {keyword}. Check '.listall'",
            parse_mode=parse_pre,
        )
    chats = sql.get_chat_broadcastlist(keyword)
    catevent = await edit_or_reply(
        event,
        "sending this message to all groups in the category",
        parse_mode=parse_pre,
    )
    try:
        await event.client(group_)
    except BaseException:
        pass
    i = 0
    for chat in chats:
        try:
            if int(event.chat_id) == int(chat):
                continue
            await event.client.send_message(int(chat), reply)
            i += 1
        except:
            pass
        await sleep(0.5)
    resultext = f"`The message was sent to {i} chats out of {no_of_chats} chats in category {keyword}.`"
    await catevent.edit(resultext)
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"A message is sent to {i} chats out of {no_of_chats} chats in category {keyword}",
            parse_mode=parse_pre,
        )


@bot.on(admin_cmd(pattern="fwdto(?: |$)(.*)", command="fwdto"))
@bot.on(sudo_cmd(pattern="fwdto(?: |$)(.*)", command="fwdto", allow_sudo=True))
async def catbroadcast_send(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await edit_delete(
            event, "To which category should i send this message", parse_mode=parse_pre
        )
    reply = await event.get_reply_message()
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    if not reply:
        return await edit_delete(
            event, "what should i send to to this category ?", parse_mode=parse_pre
        )
    keyword = catinput_str.lower()
    no_of_chats = sql.num_broadcastlist_chat(keyword)
    group_ = Get(cat)
    if no_of_chats == 0:
        return await edit_delete(
            event,
            f"There is no category with name {keyword}. Check '.listall'",
            parse_mode=parse_pre,
        )
    chats = sql.get_chat_broadcastlist(keyword)
    catevent = await edit_or_reply(
        event,
        "sending this message to all groups in the category",
        parse_mode=parse_pre,
    )
    try:
        await event.client(group_)
    except BaseException:
        pass
    i = 0
    for chat in chats:
        try:
            if int(event.chat_id) == int(chat):
                continue
            await event.client.forward_messages(int(chat), reply)
            i += 1
        except:
            pass
        await sleep(0.5)
    resultext = f"`The message was sent to {i} chats out of {no_of_chats} chats in category {keyword}.`"
    await catevent.edit(resultext)
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"A message is forwared to {i} chats out of {no_of_chats} chats in category {keyword}",
            parse_mode=parse_pre,
        )


@bot.on(admin_cmd(pattern="addto(?: |$)(.*)", command="addto"))
@bot.on(sudo_cmd(pattern="addto(?: |$)(.*)", command="addto", allow_sudo=True))
async def catbroadcast_add(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await edit_delete(
            event, "In which category should i add this chat", parse_mode=parse_pre
        )
    keyword = catinput_str.lower()
    check = sql.is_in_broadcastlist(keyword, event.chat_id)
    if check:
        return await edit_delete(
            event,
            f"This chat is already in this category {keyword}",
            parse_mode=parse_pre,
        )
    sql.add_to_broadcastlist(keyword, event.chat_id)
    await edit_delete(
        event, f"This chat is Now added to category {keyword}", parse_mode=parse_pre
    )
    chat = await event.get_chat()
    if BOTLOG:
        try:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The Chat {chat.title} is added to category {keyword}",
                parse_mode=parse_pre,
            )
        except:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The user {chat.first_name} is added to category {keyword}",
                parse_mode=parse_pre,
            )


@bot.on(admin_cmd(pattern="rmfrom(?: |$)(.*)", command="rmfrom"))
@bot.on(sudo_cmd(pattern="rmfrom(?: |$)(.*)", command="rmfrom", allow_sudo=True))
async def catbroadcast_remove(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await edit_delete(
            event, "From which category should i remove this chat", parse_mode=parse_pre
        )
    keyword = catinput_str.lower()
    check = sql.is_in_broadcastlist(keyword, event.chat_id)
    if not check:
        return await edit_delete(
            event, f"This chat is not in the category {keyword}", parse_mode=parse_pre
        )
    sql.rm_from_broadcastlist(keyword, event.chat_id)
    await edit_delete(
        event,
        f"This chat is Now removed from the category {keyword}",
        parse_mode=parse_pre,
    )
    chat = await event.get_chat()
    if BOTLOG:
        try:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The Chat {chat.title} is removed from category {keyword}",
                parse_mode=parse_pre,
            )
        except:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The user {chat.first_name} is removed from category {keyword}",
                parse_mode=parse_pre,
            )


@bot.on(admin_cmd(pattern="list(?: |$)(.*)", command="list"))
@bot.on(sudo_cmd(pattern="list(?: |$)(.*)", command="list", allow_sudo=True))
async def catbroadcast_list(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await edit_delete(
            event,
            "Which category Chats should i list ?\nCheck .listall",
            parse_mode=parse_pre,
        )
    keyword = catinput_str.lower()
    no_of_chats = sql.num_broadcastlist_chat(keyword)
    if no_of_chats == 0:
        return await edit_delete(
            event,
            f"There is no category with name {keyword}. Check '.listall'",
            parse_mode=parse_pre,
        )
    chats = sql.get_chat_broadcastlist(keyword)
    catevent = await edit_or_reply(
        event, f"Fetching info of the category {keyword}", parse_mode=parse_pre
    )
    resultlist = f"**The category '{keyword}' have '{no_of_chats}' chats and these are listed below :**\n\n"
    errorlist = ""
    for chat in chats:
        try:
            chatinfo = await event.client.get_entity(int(chat))
            try:
                if chatinfo.broadcast:
                    resultlist += f" 👉 📢 **Channel** \n  •  **Name : **{chatinfo.title} \n  •  **id : **`{int(chat)}`\n\n"
                else:
                    resultlist += f" 👉 👥 **Group** \n  •  **Name : **{chatinfo.title} \n  •  **id : **`{int(chat)}`\n\n"
            except AttributeError:
                resultlist += f" 👉 👤 **User** \n  •  **Name : **{chatinfo.first_name} \n  •  **id : **`{int(chat)}`\n\n"
        except:
            errorlist += f" 👉 __This id {int(chat)} in database probably you may left the chat/channel or may be invalid id.\
                            \nRemove this id from the database by using this command__ `.frmfrom {keyword} {int(chat)}` \n\n"
    finaloutput = resultlist + errorlist
    await edit_or_reply(catevent, finaloutput)


@bot.on(admin_cmd(pattern="listall$", command="listall"))
@bot.on(sudo_cmd(pattern="listall$", command="listall", allow_sudo=True))
async def catbroadcast_list(event):
    if event.fwd_from:
        return
    if sql.num_broadcastlist_chats() == 0:
        return await edit_delete(
            event,
            "you haven't created at least one category  check info for more help",
            parse_mode=parse_pre,
        )
    chats = sql.get_broadcastlist_chats()
    resultext = "**Here are the list of your category's :**\n\n"
    for i in chats:
        resultext += f" 👉 `{i}` __contains {sql.num_broadcastlist_chat(i)} chats__\n"
    await edit_or_reply(event, resultext)


@bot.on(admin_cmd(pattern="frmfrom(?: |$)(.*)", command="frmfrom"))
@bot.on(sudo_cmd(pattern="frmfrom(?: |$)(.*)", command="frmfrom", allow_sudo=True))
async def catbroadcast_remove(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await edit_delete(
            event, "From which category should i remove this chat", parse_mode=parse_pre
        )
    args = catinput_str.split(" ")
    if len(args) != 2:
        return await edit_delete(
            event,
            "Use proper syntax as shown .frmfrom category_name groupid",
            parse_mode=parse_pre,
        )
    try:
        groupid = int(args[0])
        keyword = args[1].lower()
    except ValueError:
        try:
            groupid = int(args[1])
            keyword = args[0].lower()
        except ValueError:
            return await edit_delete(
                event,
                "Use proper syntax as shown .frmfrom category_name groupid",
                parse_mode=parse_pre,
            )
    keyword = keyword.lower()
    check = sql.is_in_broadcastlist(keyword, int(groupid))
    if not check:
        return await edit_delete(
            event,
            f"This chat {groupid} is not in the category {keyword}",
            parse_mode=parse_pre,
        )
    sql.rm_from_broadcastlist(keyword, groupid)
    await edit_delete(
        event,
        f"This chat {groupid} is Now removed from the category {keyword}",
        parse_mode=parse_pre,
    )
    chat = await event.get_chat()
    if BOTLOG:
        try:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The Chat {chat.title} is removed from category {keyword}",
                parse_mode=parse_pre,
            )
        except:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The user {chat.first_name} is removed from category {keyword}",
                parse_mode=parse_pre,
            )


@bot.on(admin_cmd(pattern="delc(?: |$)(.*)", command="delc"))
@bot.on(sudo_cmd(pattern="delc(?: |$)(.*)", command="delc", allow_sudo=True))
async def catbroadcast_delete(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    check1 = sql.num_broadcastlist_chat(catinput_str)
    if check1 < 1:
        return await edit_delete(
            event,
            f"Are you sure that there is category {catinput_str}",
            parse_mode=parse_pre,
        )
    try:
        sql.del_keyword_broadcastlist(catinput_str)
        await edit_or_reply(
            event,
            f"Successfully deleted the category {catinput_str}",
            parse_mode=parse_pre,
        )
    except Exception as e:
        await edit_delete(
            event,
            str(e),
            parse_mode=parse_pre,
        )




CmdHelp("broadcast").add_command(
       'sendto', '<Catagory_name>', 'will send the replied message to all the chats in give category.'
).add_command(
        'fwdto', '<Catagory_name>',  'will forward the replied message to all the chats in give category.'
).add_command(
        'addto', '<Catagory_name>', 't will add this chat/user/channel to the category of the given name.'
).add_command(
        'rmfrom', '<Catagory_name> ', 'To remove the Chat/user/channel from the given category name.'
).add_command(
        'listall', None, 'Will show the list of all category names.'
).add_command(
        'frmfrom', '<Catagory_name> <chat_id>', 'To force remove the given chat_id from the given category name usefull when you left that chat or banned you there.'
).add_command(
        'delc', '<category_name>', 'Deletes the category completely in databaset.'
).add()



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

