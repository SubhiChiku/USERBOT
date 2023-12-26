from Subhi.modules.eor import eor
from Subhi.core.misc import extract_user
from pyrogram import Client, filters
from config import HANDLER as hl
from Subhi.userbot import RBX
from pyrogram.types import Message

@RBX.on_message(filters.command(["block"], hl) & filters.me)
async def block(client: Client, message: Message):
    user_id = await extract_user(message)
    bunny = await eor(message, "`ѕυвнι ση ωαу...😘`")
    if not user_id:
        return await message.edit(
            "ɢɪᴠᴇ ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʟᴏᴄᴋ..!!"
        )
    if user_id == client.me.id:
        return await bunny.edit("ɪ ᴄᴀɴ'ᴛ ʙʟᴏᴄᴋ ᴍʏsᴇʟғ ʟᴏʟ..!!")
    await client.block_user(user_id)
    geek = (await client.get_users(user_id)).mention
    await message.edit(f"__**๏ {geek} ʙʟᴏᴄᴋᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ**__")


@RBX.on_message(filters.command(["setbio"], hl) & filters.me)
async def set_bio(client: Client, message: Message):
    bunny = await eor(message, "`Processing . . .`")
    if len(message.command) == 1:
        return await bunny.edit("Provide text to set as bio..!!")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await bunny.edit(f"**Successfully Changed your BIO to..!!** `{bio}`")
        except Exception as e:
            await bunny.edit(f"**ERROR:** `{e}`")
    else:
        return await bunny.edit("Provide text to set as bio..!!")


@RBX.on_message(filters.me & filters.command(["setpfp"], hl))
async def set_pfp(client: Client, message: Message):
    replied = message.reply_to_message
    if (
        replied
        and replied.media
        and (
            replied.photo
            or (replied.document and "image" in replied.document.mime_type)
        )
    ):
        await client.download_media(message=replied, file_name=profile_photo)
        await client.set_profile_photo(profile_photo)
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
        await message.edit("**Your profile photo has been successfully changed..!!**")
    else:
        await message.edit(
            "`Reply to any photo to set as a profile photo..!!`"
        )
        await sleep(3)
        await message.delete()
