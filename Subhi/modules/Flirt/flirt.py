from pyrogram import Client, filters
from config import HANDLER as hl
from Subhi.userbot import RBX
import random
from Database.eflirt import ENGLISH
from Database.hflirt import HINDI

@RBX.on_message(filters.command("eflirt", hl) & filters.me)
async def lub(client, message):
    Y = client.me.mention
    X = random.choice(ENGLISH)
    X += f"\n\n ✍🏻 {Y} "
    await message.edit(X)

@RBX.on_message(filters.command("hflirt", hl) & filters.me)
async def lub(client, message):
    Y = client.me.mention
    X = random.choice(HINDI)
    X += f"\n\n ✍🏻 {Y} "
    await message.edit(X)
