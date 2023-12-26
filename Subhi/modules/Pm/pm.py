from pyrogram import Client, filters
from pyrogram.types import Message
from Subhi.core.basic import edit_or_reply as eor
from config import HANDLER as hl
from Database.pm import *
from config import PM_PIC
from Subhi.userbot import RBX

RABBIT = PM_PIC

pm_watcher = 5

async def get_id(_, m: Message):
    if str(m.chat.id)[0] != "-":
        return int(m.chat.id)
    if not m.reply_to_message:
        text = m.text.split()
        un_or_id = text[1]
        if un_or_id[0] == "@":
            id = (await _.get_users(un_or_id)).id
        else:
            id = int(un_or_id)
    else:
        id = m.reply_to_message.from_user.id
    return id 

TEXT ="""
๏─────────────────๏
╰๏        ⚡   яαввιтχ   ⚡            
๏─────────────────๏
╰๏ ᴛʜɪs ιѕ ᴛʜᴇ ʀᴀʙʙɪᴛx ᴘᴍ sᴇᴄᴜʀɪᴛʏ 
╰๏────────────────๏
╰๏ ᴏᴡɴᴇʀ  » {}
╰๏────────────────๏

  ᴅᴏɴ'ᴛ sᴘᴀᴍ ʜᴇʀᴇ !! ɪғ ʏᴏᴜ sᴘᴀᴍ
  ʜᴇʀᴇ ᴡɪᴛʜᴏᴜᴛ ᴍʏ ᴏᴡɴᴇʀ's
  ᴀᴘᴘʀᴏᴠᴀʟ ʏᴏᴜ ᴡɪʟʟ ʙᴇ ʙʟᴏᴄᴋᴇᴅ.

 ๏────────────────๏
╰๏ ᴡᴀʀɴs ʟɪᴍɪᴛs  » {}
╰๏────────────────๏
╰๏ ʏᴏᴜʀ ᴡᴀʀɴs  » {}
╰๏────────────────๏
╰๏     🔥 『 [ɾαႦႦιƚx](https://t.me/Robot) 』 🔥       
╰๏────────────────๏
"""

@RBX.on_message(filters.command("pmpermit", hl) & filters.me)
async def pmpro(_, m):
    x = await is_pm_on()
    try:
        tg = m.text.split()[1].lower()
    except:
        return await eor(m, f"{hl}pmpermit [ᴏɴ | ᴏғғ]")
    if not tg in ["on", "off"]:
        return await eor(m, f"{hl}pmpermit [ᴏɴ | ᴏғғ]")
    if tg == "on":
        if x:
            return await eor(m,"ᴘᴍᴘᴇʀᴍɪᴛ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ ʟᴏʟ..!!")
        await toggle_pm()
        if await limit() == 0:
            await update_warns(3)
        return await eor(m,"ᴘᴍᴘᴇʀᴍɪᴛ ᴇɴᴀʙʟᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ..!! !")
    if not x:
        return await eor(m,"ᴘᴍᴘᴇʀᴍɪᴛ ɪsɴ'ᴛ ᴇɴᴀʙʟᴇᴅ ᴀɴʏᴍᴏʀᴇ..!!")
    await toggle_pm()
    return await eor(m,"ᴘᴍᴘᴇʀᴍɪᴛ ᴅɪsᴀʙʟᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ..!!")

@RBX.on_message(filters.command(["approve", "disapprove", "a", "da", "allow", "disallow"], hl) & filters.me)
async def appro_dis(_, m):
    if str(m.chat.id)[0] == "-":
        try:
            id = await get_id(_, m)
        except:
            return await eor(m, "ʀᴇᴘʟʏ ᴛᴏ sᴏᴍᴇᴏɴᴇ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ɪᴅ ᴛᴏ ᴀ ᴏʀ ᴅᴀ..!!")
    else:
        id = m.chat.id
    tg = m.text.split()[0][1]
    x = await is_approved(id)
    if tg == "d":
        if not x:
            return await eor(m,"ᴜsᴇʀ ᴡᴀsɴ'ᴛ ᴀᴘᴘʀᴏᴠᴇᴅ ʏᴇᴛ..!!")
        await disapprove(id)
        return await eor(m,"ᴅɪsᴀᴘᴘʀᴏᴠᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴜsᴇʀ ᴛᴏ ᴘᴍ..!!")
    if x:
        return await eor(m,"ᴜsᴇʀ ᴀʟʀᴇᴀᴅʏ ᴀᴘᴘʀᴏᴠᴇᴅ ɪɴ ᴘᴍ ʟᴏʟ..!!")
    await approve(id) 
    await reset_warns(id)
    return await eor(m,"ᴜsᴇʀ sᴜᴄᴄᴇssғᴜʟʟʏ ᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ..!!")

@RBX.on_message(filters.command("setwarns", hl) & filters.me)
async def setter(_, m):
    try:
        count = int(m.text.split()[1])
    except:
        return await eor(m, f"{hl}setwarns [ᴠᴀʟᴜᴇ]")
    if count == 0:
        return await eor(m, "ɢɪᴠᴇ sᴏᴍᴇ ᴠᴀʟᴜᴇ ᴀʙᴏᴠᴇ 0 ᴛᴏ sᴇᴛ ᴀs ᴡᴀʀɴ ʟɪᴍɪᴛ..!!")
    await update_warns(count)
    await eor(m, f"ᴘᴍ ᴡᴀʀɴs sᴜᴄᴄᴇssғᴜʟʟʏ sᴇᴛ ᴀs {count} ..!!")


@RBX.on_message(filters.private, group=pm_watcher)
async def cwf(_, m):
    user_ = m.from_user
    if not await is_pm_on():
        return
    if user_.is_bot:
        return
    if m.from_user.id == _.me.id:
        return
    if await is_approved(m.from_user.id):
        return
    await add_warn(m.from_user.id)
    if await limit() <= await get_warns(m.from_user.id):
        await m.reply("sᴘᴀᴍᴍᴇʀ ᴅɪʀᴇᴄᴛᴇᴅ ᴀɴᴅ ʙʟᴏᴄᴋᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ..!!")
        await reset_warns(m.from_user.id)
        return await _.block_user(m.from_user.id)
    await m.reply_photo(RABBIT, caption=TEXT.format((await _.get_me()).first_name, await limit(), await get_warns(m.from_user.id)))
