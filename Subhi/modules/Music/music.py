import asyncio
from pyrogram import filters
from pyrogram.types import Message
from Subhi.userbot import RBX
from Subhi.core.PyroHelpers import ReplyCheck
from config import HANDLER as hl

@RBX.on_message(filters.command(["m", "music"], hl) & filters.me)
async def send_music(bot: RBX, message: Message):
    try:
        cmd = message.command

        song_name = ""
        if len(cmd) > 1:
            song_name = " ".join(cmd[1:])
        elif message.reply_to_message and len(cmd) == 1:
            song_name = (
                    message.reply_to_message.text or message.reply_to_message.caption
            )
        elif not message.reply_to_message and len(cmd) == 1:
            await message.edit("Give a song name..!!")
            await asyncio.sleep(2)
            await message.delete()
            return

        song_results = await RBX.get_inline_bot_results("deezermusicbot", song_name)

        try:
            saved = await bot.send_inline_bot_result(
                chat_id="me",
                query_id=song_results.query_id,
                result_id=song_results.results[0].id,
            )

            saved = await RBX.get_messages("me", int(saved.updates[1].message.id))
            reply_to = (
                message.reply_to_message.id
                if message.reply_to_message
                else None
            )
            await bot.send_audio(
                chat_id=message.chat.id,
                audio=str(saved.audio.file_id),
                reply_to_message_id=ReplyCheck(message),
            )
            await RBX.delete_messages("me", saved.id)
        except TimeoutError:
            await message.edit("That didn't work anymore..!!")
            await asyncio.sleep(2)
        await message.delete()
    except Exception as e:
        print(e)
        await message.edit("`Failed to find song..!!`")
        await asyncio.sleep(2)
        await message.delete()
