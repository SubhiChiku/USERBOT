from pyrogram.types import Message
from config import HANDLER as hl
from Subhi.core.basic import get_text
import requests
from pyrogram import Client, filters
from Subhi.userbot import RBX

@RBX.on_message(filters.command("trump", hl) & filters.me)
async def tweet(client: Client, message: Message):
    text = get_text(message)
    if not text:
        await message.edit(f"`ɢɪᴠᴇ ᴍᴇ sᴏᴍᴛʜɪɴɢ ᴛᴏ ᴛᴡᴇᴇᴛ..!!`")
        return
    url = f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}"
    r = requests.get(url=url).json()
    tweet = r["message"]
    await message.edit(f"`ᴛʀᴜᴍᴘ ɪs ᴛᴡᴇᴇᴛɪɴɢ...💥`")
    await client.send_photo(message.chat.id, tweet)
    await message.delete()
