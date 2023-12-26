"""
from pyrogram import Client, filters
import openai
from Subhi.userbot import RBX
from config import HANDLER as hl

@RBX.on_message(filters.command("ask", hl) & filters.me)
async def ask_ai(client, message):
    try:
        query = message.text.split("ask", 1)[1].strip()

        brand_api_key = "YOUR_BRAND_API_KEY"

        response = requests.post('https://api.openai.com/v1/engines/davinci/completions',
                                 headers={'Authorization': f'Bearer {brand_api_key}'},
                                 json={
                                     'prompt': query,
                                     'max_tokens': 150
                                 })
        data = response.json()
        await message.reply_text(data['choices'][0]['text'].strip())
    except Exception as e:
        print(e)
        await message.reply_text("Failed to generate a response. Please try again..!!")
    """
