from pyrogram import Client, filters
import requests
from Subhi.userbot import RBX
from config import HANDLER as hl

NEWS_API_KEY = "140dd16908d54879b350d0c7378306a5"

@RBX.on_message(filters.command("news", hl) & filters.me)
async def get_news(client, message):
    try:
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}")
        news_data = response.json()

        headlines = ""
        for article in news_data["articles"][:5]:
            headlines += f"📰 {article['title']}\n\n"

        await message.edit(headlines)
    except Exception as e:
        print(e)
        await message.edit("Failed to fetch the news. Please try again later..!!")
