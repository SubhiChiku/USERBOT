import asyncio
from pyrogram import filters
from pyrogram.types import Message
from Subhi.userbot import RBX
from config import HANDLER as hl


@RBX.on_message(filters.command(["l", "lyrics"], hl) & filters.me)
async def send_lyrics(bot: RBX, message: Message):
    try:
        cmd = message.command

        song_name = ""
        if len(cmd) > 1:
            song_name = " ".join(cmd[1:])
        elif message.reply_to_message:
            if message.reply_to_message.audio:
                song_name = f"{message.reply_to_message.audio.title} {message.reply_to_message.audio.performer}"
            elif len(cmd) == 1:
                song_name = message.reply_to_message.text
        elif not message.reply_to_message and len(cmd) == 1:
            await message.edit("Give a song name..!!")
            await asyncio.sleep(2)
            await message.delete()
            return

        await message.edit(f"Getting lyrics for `{song_name}`..!!")
        lyrics_results = await RBX.get_inline_bot_results("ilyricsbot", song_name)

        try:
            saved = await bot.send_inline_bot_result(
                chat_id="me",
                query_id=lyrics_results.query_id,
                result_id=lyrics_results.results[0].id,
            )
            await asyncio.sleep(3)
            await bot.copy_message(
                chat_id=message.chat.id,
                from_chat_id="me",
                message_id=saved.updates[1].message.id,
            )
            await bot.delete_messages("me", saved.updates[1].message.id)
        except TimeoutError:
            await message.edit("That didn't work anymore..!!")
            await asyncio.sleep(2)
        await message.delete()
    except Exception as e:
        await message.edit("`Failed to find lyrics..!!`")
        await asyncio.sleep(2)
        await message.delete()
