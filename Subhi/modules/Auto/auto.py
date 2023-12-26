from pyrogram import filters
from pyrogram.types import Message
from Subhi.userbot import RBX
from config import HANDLER as hl

the_regex = r"^r\/([^\s\/])+"
x = filters.chat([])
@RBX.on_message(x)
async def auto_read(bot: RBX, message: Message):
    await RBX.read_chat_history(message.chat.id)
    message.continue_propagation()

@RBX.on_message(filters.command("autoread", hl) & filters.me)
async def auto(bot: RBX, message: Message):
    if message.chat.id in x:
        x.remove(message.chat.id)
        await message.edit("Autoread deactivated..!!")
    else:
        x.add(message.chat.id)
        await message.edit("Autoread activated..!!")
