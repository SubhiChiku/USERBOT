from pyrogram import Client, filters
from config import HANDLER as hl
from Subhi.userbot import RBX
import random
from Database.love import LOVE

@RBX.on_message(filters.command("iloveu", hl) & filters.me)
async def lub(client, message):
    X = random.choice(LOVE)
    await message.edit(X)
