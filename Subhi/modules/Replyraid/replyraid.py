import random
from config import HANDLER as hl
import asyncio
from Database.replyraid import *
from pyrogram import Client, filters
from Subhi.userbot import RBX
from Database.raid import RAID

@RBX.on_message(filters.command("replyraid", hl) & filters.me)
async def replyraid(_, m):
    try:
        if m.reply_to_message:
            id = m.reply_to_message.from_user.id
        else:
            x = m.text.split()[1]
            if str(x)[0] == "@":
                id = (await _.get_users(x)).id
            else:
                id = int(x)
    except:
        return await m.edit(f"`{hl}replyraid [ɪᴅ|ᴜsᴇʀɴᴀᴍᴇ|ʀᴇᴘʟʏ]`")
    if await is_rr(id):
        return await m.edit("`ʀᴀɪᴅ ɪs ᴀʟʀᴇᴀᴅʏ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴛᴏ ᴛʜɪs ᴜsᴇʀ..!!`")
    await add_rr(id)
    return await m.edit(f"`ʀᴇᴘʟʏʀᴀɪᴅ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴛᴏ ᴜsᴇʀ..!!` <code>{id}</code>")
 
@RBX.on_message(filters.command("dreplyraid", hl) & filters.me)
async def dreplyraid(_, m):
    try:
        if m.reply_to_message:
            id = m.reply_to_message.from_user.id
        else:
            x = m.text.split()[1]
            if str(x)[0] == "@":
                id = (await _.get_users(x)).id
            else:
                id = int(x)
    except:
        return await m.edit(f"`{hl}dreplyraid [ɪᴅ|ᴜsᴇʀɴᴀᴍᴇ|ʀᴇᴘʟʏ]`")
    if not await is_rr(id):
        return await m.edit("`ʀᴀɪᴅ ɪs ɴᴏᴛ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴛᴏ ᴛʜɪs ᴜsᴇʀ..!!`")
    await del_rr(id)
    return await m.edit(f"`ʀᴇᴘʟʏʀᴀɪᴅ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴛᴏ ᴜsᴇʀ..!!` <code>{id}</code>")

@RBX.on_message(group=2)
async def raid_cwf(_, m):
    if m.from_user:
        if await is_rr(m.from_user.id):
            await m.reply(random.choice(RAID))
