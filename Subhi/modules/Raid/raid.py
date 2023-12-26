from pyrogram import Client, filters
from Database.raid import *
import random 
from Subhi.userbot import RBX
from config import HANDLER as hl
from Subhi.modules.eor import eor

@RBX.on_message(filters.command("raid", hl) & filters.me)
async def raid(client, message):
    usage = f"{hl}raid [ᴄᴏᴜɴᴛ] [ʀᴇᴘʟʏ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ]"
    try:
        if message.reply_to_message:
            count = int(message.text.split()[1])
            id = message.reply_to_message.from_user.id
        else:
            count = int(message.text.split()[1])
            txt = message.text.split()[2]
            try:
                id = int(txt)
            except:
                id = (await client.get_users(txt)).id
    except:
        return await eor(message, usage)
    user = (await client.get_users(id)).mention
    for i in range(0, count):
        await client.send_message(message.chat.id, f" {user}" +random.choice(RAID))
