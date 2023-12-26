from pyrogram import Client, filters
from config import HANDLER as hl
from Subhi.userbot import RBX
import random 
import asyncio
from pyrogram.types import Message

@RBX.on_message(filters.command("stupid", hl) & filters.me)
async def stupid(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 14)
    await message.edit("brain")
    animation_chars = [
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           (> ^_^)>🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           <(^_^ <)🗑",
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 14])

@RBX.on_message(filters.command(["dick", "muth"], hl) & filters.me)
async def muthal(client: Client, message: Message):
    e = await message.edit("8✊===D")
    await e.edit("8=✊==D")
    await e.edit("8==✊=D")
    await e.edit("8===✊D")
    await e.edit("8==✊=D")
    await e.edit("8=✊==D")
    await e.edit("8✊===D")
    await e.edit("8=✊==D")
    await e.edit("8==✊=D")
    await e.edit("8===✊D")
    await e.edit("8==✊=D")
    await e.edit("8=✊==D")
    await e.edit("8✊===D")
    await e.edit("8=✊==D")
    await e.edit("8==✊=D")
    await e.edit("8===✊D")
    await e.edit("8==✊=D")
    await e.edit("8=✊==D")
    await e.edit("8===✊D💦")
    await e.edit("8==✊=D💦💦")
    await e.edit("8=✊==D💦💦💦")
    await e.edit("8✊===D💦💦💦💦")
    await e.edit("8===✊D💦💦💦💦💦")
    await e.edit("8==✊=D💦💦💦💦💦💦")
    await e.edit("8=✊==D💦💦💦💦💦💦💦")
    await e.edit("8✊===D💦💦💦💦💦💦💦💦")
    await e.edit("8===✊D💦💦💦💦💦💦💦💦💦")
    await e.edit("8==✊=D💦💦💦💦💦💦💦💦💦💦")
    await e.edit("8=✊==D__ MUTH KA PANI KHATAM..!!💀__")
    await e.edit("__MAR GYA MUTHAL__🥲")


@RBX.on_message(filters.command(["sayang", "lover"], hl) & filters.me)
async def lovers(client: Client, message: Message):
    e = await message.edit("I LOVEE YOUUU 💕")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💗💕")
    await e.edit("💘💞💕💗")
    await e.edit("LOVE YOU 💝💖💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💕💗")
    await e.edit("LOVE")
    await e.edit("YOU")
    await e.edit("FOREVER 💕")
    await e.edit("💘💘💘💘")
    await e.edit("LOVE")
    await e.edit("I")
    await e.edit("LOVE")
    await e.edit("BABY")
    await e.edit("I LOVE YOUUUU")
    await e.edit("MY BABY")
    await e.edit("💕💞💘💝")
    await e.edit("💘💕💞💝")
    await e.edit("LOVE YOU 💞")

@RBX.on_message(filters.command("dead", hl) & filters.me)
async def dead(client: Client, message: Message):
    await message.edit(
        "`Drugs Everything...`          \n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n",
    )
