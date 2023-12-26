from pyrogram import Client, filters
from Subhi.userbot import RBX
from pyrogram.types import Message
from Subhi import startTime
from Subhi import get_uptime
import time 
from config import HANDLER as hl

def grt(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

@RBX.on_message(filters.command("ping",  hl) & filters.me)
async def ping(client, message):
    r = await client.get_me()
    st = time.time()
    end = time.time()
    user = r.mention
    upt = get_uptime(time.time())
    pong = str((end-st)*1000)[0:5]
    gtr = grt(int(time.time()-startTime))
    PING = f"""
__𝗣𝗢𝗡𝗚 🏓__

__**๏ ᴘɪɴɢ »**__ `{pong}`
__**๏ ᴜᴘᴛɪᴍᴇ »**__ `{upt}`
**__๏ ᴏᴡɴᴇʀ »__** {user}
"""
    return await message.edit(PING)
