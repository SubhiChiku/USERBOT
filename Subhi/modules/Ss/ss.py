import asyncio
from pyrogram import filters
from pyrogram.raw import functions
from pyrogram.types import Message
from Subhi.userbot import RBX
from config import HANDLER as hl

@RBX.on_message(filters.command(["screenshot", "ss"], hl) & filters.private & filters.me)
async def screenshot(bot: RBX, message: Message):
    await asyncio.gather(
        message.delete(),
        bot.invoke(
            functions.messages.SendScreenshotNotification(
                peer=await RBX.resolve_peer(message.chat.id),
                reply_to_msg_id=0,
                random_id=RBX.rnd_id(),
            )
        ),
    )
