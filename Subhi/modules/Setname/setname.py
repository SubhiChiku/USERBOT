from Subhi.core.basic import edit_or_reply
from Subhi.core.misc import extract_user
from pyrogram import Client, filters
from config import HANDLER as hl
from Subhi.userbot import RBX
from pyrogram.types import Message

@RBX.on_message(filters.command(["setname"], hl) & filters.me)
async def name(client: Client, message: Message):
    bunny = await edit_or_reply(message, "`ѕυвнι ση ωαу...😘`")
    if len(message.command) == 1:
        return await bunny.edit(
            "ɢɪᴠᴇ ᴍᴇ ᴛʜᴀᴛ ɴᴀᴍᴇ..!!"
        )
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await bunny.edit(f"**__๏ {name} sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ɴᴀᴍᴇ..!!__**")
        except Exception as e:
            await bunny.edit(f"**__๏ ᴇʀʀᴏʀ »__** `{e}`")
    else:
        return await bunny.edit(
            "ɢɪᴠᴇ ᴍᴇ ᴀ ᴛʜᴀᴛ ᴛᴇxᴛ..!!"
        )
