import sys
import logging
from os import environ, execle, remove
from pyrogram import Client, filters
from pyrogram.types import Message
from Subhi.core.basic import eor
from config import HANDLER as hl
from Subhi.userbot import RBX

GEEK = None

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


@RBX.on_message(filters.command("restart", hl) & filters.me)
async def restart_bot(_, message: Message):
    try:
        msg = await eor(message, "`Restarting bot...`")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("__UB has been restarted Successfully..!!__\n\n")
    if GEEK is not None:
        GEEK.restart()
    else:
        args = [sys.executable, "-m", "Subhi"]
        execle(sys.executable, *args, environ)
