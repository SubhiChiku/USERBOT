from pyrogram import Client, enums, filters
from pyrogram.types import Message
from config import BLACKLIST_CHAT
from config import HANDLER as hl
from Subhi.core.basic import edit_or_reply
from Subhi.userbot import RBX

@RBX.on_message(filters.command("join", hl) & filters.me)
async def join(client: Client, message: Message):
    bunny = message.command[1] if len(message.command) > 1 else message.chat.id
    rabbit = await edit_or_reply(message, "`Processing...`")
    try:
        await rabbit.edit(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴊᴏɪɴᴇᴅ ** `{bunny}` ⚡")
        await client.join_chat(bunny)
    except Exception as ex:
        await rabbit.edit(f"**ᴇʀʀᴏʀ:** \n\n{str(ex)}")


@RBX.on_message(filters.command(["leave", "kickme"], hl) & filters.me)
async def leave(client: Client, message: Message):
    bunny = message.command[1] if len(message.command) > 1 else message.chat.id
    rabbit = await edit_or_reply(message, "`Processing...`")
    if message.chat.id in BLACKLIST_CHAT:
        return await rabbit.edit("**__ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ɴᴏᴛ ᴜsᴇᴅ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ..!!__**")
    try:
        await rabbit.edit_text(f"**__{client.me.first_name}  ʜᴀs ʟᴇғᴛ ᴛʜɪs ɢʀᴏᴜᴘ, ʙʏᴇ ʙʏᴇ 😪 !!**__")
        await client.leave_chat(bunny)
    except Exception as ex:
        await rabbit.edit_text(f"**ᴇʀʀᴏʀ:** \n\n{str(ex)}")


@RBX.on_message(filters.command(["leaveallgc"], hl) & filters.me)
async def kickmeall(client: Client, message: Message):
    bunny = await edit_or_reply(message, "`ʟᴇᴀᴠɪɴɢ ᴀʟʟ ɢʀᴏᴜᴘ ᴄʜᴀᴛs...⚡`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await bunny.edit(
        f"__**๏ sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇᴀᴠᴇ {done} ɢʀᴏᴜᴘ ⚡\n\n๏ ғᴀɪʟᴇᴅ ᴛᴏ ʟᴇᴀᴠᴇ {er} ɢʀᴏᴜᴘ ⚡**__"
    )


@RBX.on_message(filters.command(["leaveallch"], hl) & filters.me)
async def kickmeallch(client: Client, message: Message):
    bunny = await edit_or_reply(message, "`ʟᴇᴀᴠɪɴɢ ᴀʟʟ ᴄʜᴀɴɴᴇʟs...⚡`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await bunny.edit(
        f"__**๏ sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇᴀᴠᴇ {done} ᴄʜᴀɴɴᴇʟ ⚡\n\n๏ ғᴀɪʟᴇᴅ ᴛᴏ ʟᴇᴀᴠᴇ {er} ᴄʜᴀɴɴᴇʟ ⚡**__"
    )
