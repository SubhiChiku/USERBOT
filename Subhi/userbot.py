from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION

bot = Client(
     name="bOt",
     api_id=API_ID,
     api_hash=API_HASH,
     bot_token=BOT_TOKEN
   )

RBX = Client(name="bunny", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)
