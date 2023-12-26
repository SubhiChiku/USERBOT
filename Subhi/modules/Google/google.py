"""
from pyrogram import Client, filters
from googlesearch import search
from Subhi.userbot import RBX
from config import HANDLER as hl

@RBX.on_message(filters.command("google", hl) & filters.me)
async def google_search(client, message):
    query = message.text.split(maxsplit=1)[1]
    search_results = search(query, stop=5, pause=2)
    response = f"Here are the top 5 search results for '{query}':\n\n"
    for result in search_results:
        response += f"- {result}\n"
    await message.edit(response)
"""
