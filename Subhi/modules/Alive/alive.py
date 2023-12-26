import time
from pyrogram import Client, filters
from Subhi import startTime
from Subhi.userbot import RBX
import asyncio
from Subhi import get_uptime
from Subhi import ALIVE_PIC
from pyrogram import __version__ as py_version
version = "v1.0"
from platform import python_version
from Subhi.modules.eor import eor
from config import HANDLER as hl

@RBX.on_message(filters.command("alive",  hl) & filters.me )
async def alive(client, message):
    sex = await eor(message,"`ρяσƈҽʂʂιɳɠ....⚡`")
    await asyncio.sleep(0.3)
    user = (await client.get_me()).mention
    upt = get_uptime(time.time())
    await sex.edit("`яαввιтχ ιѕ αℓινє...⚡`")
    await asyncio.sleep(0.3)
    await sex.edit("`gєттιиg вσт ∂єтαιℓѕ...⚡`")
    aliver = f"""
╭────────────────๏
╰๏⚡ __**яαввιтχ ιѕ αℓινє**__ ⚡
╭────────────────๏
╰๏ **__σωиєя »__** {user}
╰๏ __**ρуяσgяαм »__** `{py_version}`
╰๏ __**яαввιтχ »**__ `{version}`
╰๏ __**ρутнσи »__** `{python_version()}`
╰๏ __**υρтιмє »__** `{upt}`
╰────────────────๏
╰๏      【[ƚԋҽ ɾαႦႦιƚx](https://t.me/RoBotXUpdates)】       
╰────────────────๏
"""
    await asyncio.sleep(0.3)
    await sex.delete()
    await message.reply_photo(ALIVE_PIC, caption=aliver)
