from Subhi.core.basic import edit_or_reply
from Subhi.core.misc import extract_user
from pyrogram import Client, filters
from config import HANDLER as hl
from Subhi.userbot import RBX
from pyrogram.types import Message

@RBX.on_message(filters.command(["unblock"], hl) & filters.me)
async def unblock(client: Client, message: Message):
    user_id = await extract_user(message)
    bunny = await edit_or_reply(message, "`ѕυвнι ση ωαу...😘`")
    if not user_id:
        return await message.edit(
            "ɢɪᴠᴇ ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴜɴʙʟᴏᴄᴋ ᴛʜᴀᴛ ᴜsᴇʀ..!!**."
        )
    if user_id == client.me.id:
        return await bunny.edit("ɪ ᴄᴀɴ'ᴛ ᴜɴʙʟᴏᴄᴋ ᴍʏsᴇʟғ ʟᴏʟ...!!")
    await client.unblock_user(user_id)
    geek = (await client.get_users(user_id)).mention
    await message.edit(f"**__๏ {geek} ᴜɴʙʟᴏᴄᴋᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ..!!__**")
