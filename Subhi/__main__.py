from Subhi.userbot import RBX, bot
import asyncio
import time
import importlib
from pyrogram import Client, idle
from Subhi.modules import ALL_MODULES

async def start_user():
    await bot.start()
    print("[•RBX•]: єνєяутнιиg ιѕ σк, ѕтαятιиg... уσυя υѕєявσт ρℓєαѕє ωαιт... ⚡")
    for all_module in ALL_MODULES:
        importlib.import_module("Subhi.modules" + all_module)
        print(f"[•RBX•] ѕυ¢¢єѕѕfυℓℓу ιмρσятє∂ {all_module} ⚡")
    await RBX.start()
    x = await RBX.get_me()
    print(f"υѕєявσт ѕυ¢¢єѕѕfυℓℓყ ѕтαятє∂ αѕ {x.first_name} ⚡ ")
    try:
     await RBX.join_chat("SUBI_WORLD")
     await RBX.join_chat("RoBotXUpdates")
    except:
      pass
    try:
     await RBX.send_message(-1002084534383, "__**ѕтαятє∂ !!**__")
    except:
      pass
    await idle()
  
loop = asyncio.get_event_loop()
loop.run_until_complete(start_user())
