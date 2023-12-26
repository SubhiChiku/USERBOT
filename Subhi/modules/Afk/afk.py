from pyrogram import Client, filters
from Subhi.modules.eor import eor
from Database.afk import *
import time
from Subhi.modules.Afk import grt, my_info
from config import HANDLER as hl
from Subhi.userbot import RBX

afk_watcher = 6

@RBX.on_message(filters.command('afk', hl) & filters.me)
async def afk(_, m):
  reason = m.text.split(None, 1)[1] if len(m.command) > 1 else ''
  tim = time.time()
  txt = "see yaa !, am afk" + "\n\n" + f"**reason:** `{reason}`" if reason else "see yaa !, am afk"
  await eor(m, txt)
  await add_afk({"afk_time": tim, "afk_reason": reason})

@RBX.on_message(group=afk_watcher)
async def cwf(_, m):
  if not await is_afk():
    return
  det = await get_afk_details()
  me = await my_info()
  if m.from_user.is_self:
    if m.text:
      if m.text.lower().startswith(f'{hl}afk'):
        return
    txt = "I'm back online..!! afk for" + f' `{grt(int(time.time() - det[0]))}`.'
    if det[1]:
      txt += "\n\n"
      txt += "**reason:**" + f" `{det[1]}`"
    await _.send_message(m.chat.id, txt)
    return await remove_afk()
  user_id = m.from_user.id if m.from_user else 0
  if m.chat.id > 0:
    txt = "I'm afk..!! since" + f' `{grt(int(time.time() - det[0]))}`.'
    if det[1]:
      txt += "\n\n"
      txt += "**reason:**" + f" `{det[1]}`"
    return await m.reply(txt)
  reply = m.reply_to_message
  if reply:
    if reply.from_user.id != _.me.id:
      return
    txt = "I'm afk..!! since" + f' `{grt(int(time.time() - det[0]))}`.'
    if det[1]:
      txt += "\n\n"
      txt += "**reason:**" + f" `{det[1]}`"
    return await m.reply(txt)
  entities = m.entities
  if entities:
    for entity in entities:
      if entity.type.name == "MENTION":
        text = m.text if m.text else m.caption
        text = text.split()
        for tex in text:
          if tex[0] != "@":
            continue
          try:
            id = (await _.get_users(tex)).id
          except:
            continue
          if id != _.me.id:
            continue
          txt = "I'm afk..!! since" + f' `{grt(int(time.time() - det[0]))}`.'
          if det[1]:
            txt += "\n\n"
            txt += "**reason:**" + f" `{det[1]}`"
          return await m.reply(txt)
      if entity.type.name == "TEXT_MENTION":
        if entity.user.id != me.id:
          return
        txt = "I'm afk..!; since" + f' `{grt(int(time.time() - det[0]))}`.'
        if det[1]:
          txt += "\n\n"
          txt += "**reason:**" + f" `{det[1]}`"
        return await m.reply(txt)
