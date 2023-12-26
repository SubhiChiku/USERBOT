from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from config import HANDLER as hl
import time
from pyrogram import Client, filters
from Subhi.userbot import bot
from config import HELP_PIC
from Subhi.userbot import RBX
from pyrogram.types import InlineQueryResultPhoto as IQRP

PIC = HELP_PIC

HELP_TEXT = "ᴛʜɪs ɪs ʀᴀʙʙɪᴛx ᴜsᴇʀʙᴏᴛ ʜᴇʟᴘ ᴍᴇɴᴜ..!!\n\n ʜᴏᴍᴇ ᴘᴀɢᴇ "

HELP_TEXT2 = "ᴛʜɪs ɪs ʀᴀʙʙɪᴛx ᴜsᴇʀʙᴏᴛ ʜᴇʟᴘ ᴍᴇɴᴜ..!!\n\n 2ɴᴅ ᴘᴀɢᴇ "

HELP_TEXT3 = "ᴛʜɪs ɪs ʀᴀʙʙɪᴛx ᴜsᴇʀʙᴏᴛ ʜᴇʟᴘ ᴍᴇɴᴜ..!!\n\n 3ʀᴅ ᴘᴀɢᴇ "

ADMINS_MSG = f"""
**ᴀᴅᴍɪɴs ʜᴇʟᴘ ᴍᴇɴᴜ**

๏ `{hl}ban` » ᴛᴏ ʙᴀɴ ᴀɴʏ ᴍᴇᴍʙᴇʀ..!! 

๏ `{hl}unban` » ᴛᴏ ᴜɴʙᴀɴ ᴀɴʏ ᴍᴇᴍʙᴇʀ..!!

๏ `{hl}mute` » ᴛᴏ ᴍᴜᴛᴇ ᴀɴʏ ᴍᴇᴍʙᴇʀ..!!

๏ `{hl}unmute` » ᴛᴏ ᴜɴᴍᴜᴛᴇ any ᴍᴇᴍʙᴇʀ..!! 

๏ `{hl}kick` » ᴛᴏ ᴋɪᴄᴋ ᴀɴʏ ᴍᴇᴍʙᴇʀ..!! 

๏ `{hl}pin` » ᴛᴏ ᴘɪɴ ᴀɴʏ ᴍᴇssᴀɢᴇ..!! 

๏ `{hl}unpin` » ᴛᴏ ᴜɴᴘɪɴ ᴀɴʏ ᴍᴇssᴀɢᴇ..!! 

๏ `{hl}promote` » ᴛᴏ ᴘʀᴏᴍᴏᴛᴇ ᴀɴʏᴏɴᴇ..!! 

๏ `{hl}demote` » ᴛᴏ ᴅᴇᴍᴏᴛᴇ ᴀɴʏᴏɴᴇ..!!

"""

EXTRA_MSG = f"""
**ᴇxᴛʀᴀ ʜᴇʟᴘ ᴍᴇɴᴜ** 

๏ `{hl}ping` » ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴘɪɴɢ..!!

๏ `{hl}alive` » ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ..!!

๏ `{hl}repo` » ᴛᴏ ɢᴇᴛ ʙᴏᴛ ʀᴇᴘᴏ..!!

๏ `{hl}ss` » ᴛᴏ ғᴀᴋᴇ ss ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ..!!

๏ `{hl}chance` » ᴏɴʟʏ ғᴜɴ

๏ `{hl}ani` » ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀɴɪᴍᴀᴛᴇᴅ ǫ

๏ `{hl}q` » ᴛᴏ ᴄʀᴇᴀᴛᴇ ǫ
"""

INVITE_MSG = f"""
**ɪɴᴠɪᴛᴇ ʜᴇʟᴘ ᴍᴇɴᴜ**
๏ `{hl}invite` » ᴛᴏ ɪɴᴠɪᴛᴇ ᴍᴇᴍʙᴇʀ ʙʏ ᴜsᴇʀɴᴀᴍᴇ..!!

๏ `{hl}invitelink` » ᴛᴏ ɢᴇᴛ ɪɴᴠɪᴛᴇ ʟɪɴᴋ ᴏғ ɢᴄ..!!

๏ `{hl}inviteall` » ᴛᴏ ɪɴᴠɪᴛᴇ ᴀʟʟ ᴍᴇᴍʙᴇʀ ᴏғ ᴀɴᴏᴛʜᴇʀ ɢᴄ..!!

"""
AFK_MSG = f"""
**ᴀғᴋ ʜᴇʟᴘ ᴍᴇɴᴜ**

๏ `{hl}afk` » ᴛᴏ ᴀᴄᴛɪᴠᴀᴛᴇ ᴀғᴋ..!!

"""

IMPORT_MSG = f"""
**ɪᴍᴘᴏʀᴛᴀɴᴛ ʜᴇʟᴘ ᴍᴇɴᴜ**

๏ `{hl}tts` » ᴛᴏ ᴛᴇxᴛ ᴛᴏ ᴠᴏɪᴄᴇ ᴀɴʏ ᴍᴇssᴀɢᴇ..!!

๏ `{hl}music` » ᴛᴏ ɢᴇᴛ ᴀɴʏ ᴍᴜsɪᴄ ʙʏ ɪᴛ's ɴᴀᴍᴇ..!!

๏ `{hl}lyrics` » ᴛᴏ ɢᴇᴛ ᴀɴʏ sᴏɴɢ ʟʏʀɪᴄs..!!

๏ `{hl}weather` » ᴛᴏ ɢᴇᴛ ᴡᴇᴀᴛʜᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ..!!

๏ `{hl}news` » ᴛᴏ ɢᴇᴛ ɪɴᴅɪᴀɴ ɴᴇᴡs..!!

๏ `{hl}autoread` » ᴛᴏ ᴀᴄᴛɪᴠᴀᴛᴇ ᴀᴜᴛᴏ ᴍᴇssᴀɢᴇ ʀᴇᴀᴅ..!!

๏ `{hl}carbon` » ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ ᴏғ ɢɪᴠᴇɴ ᴛᴇxᴛ..!!

๏ `{hl}paste` » ᴛᴏ ᴘᴀsᴛᴇ ᴀɴʏ ғɪʟᴇ ɪɴ ᴘɪᴄ
"""

DM_MSG = f"""
ᴘᴍ ʜᴇʟᴘ ᴍᴇɴᴜ

๏ `{hl}pmpermit` » ᴛᴏ ᴏɴ & ᴏғғ ᴘᴍᴘᴇʀᴍɪᴛ..!!

๏ `{hl}setwarns` » ᴛᴏ sᴇᴛ ᴡᴀʀɴ ᴏғ ᴘᴍᴘᴇʀᴍɪᴛ..!! 

๏ `{hl}a` » ᴛᴏ ᴀᴘᴘʀᴏᴠᴇ ᴀɴʏᴏɴᴇ ɪɴ ᴘᴍ..!!

๏ `{hl}da` » ᴛᴏ ᴅɪsᴀᴘᴘʀᴏᴠᴇ ᴀɴʏᴏɴᴇ ɪɴ ᴘᴍ..!!
"""

SEC_MSG = f"""
"*sᴇᴄʀᴇᴛ ʜᴇʟᴘ ᴍᴇɴᴜ**

๏ `{hl}wow` » ᴛᴏ sᴀᴠᴇ ᴛɪᴍᴇʀ ᴘɪᴄ ᴘᴇʀᴍᴀɴᴇɴᴛʟʏ..!!

๏ `{hl}restart` » ᴛᴏ ʀᴇsᴛᴀʀᴛ ᴜsᴇʀʙᴏᴛ..!!

๏ `{hl}adminlist` » ᴛᴏ ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴs..!!

๏ `{hl}eval` » ᴛᴏ ʀᴜɴ ᴘʏᴛʜᴏɴ ᴄᴏᴅᴇs..!!

๏ `{hl}mystats` » to check your current stats..!!
"""

STK_MSG = f"""
**sᴛɪᴄᴋᴇʀ ʜᴇʟᴘ ᴍᴇɴᴜ**

๏ `{hl}kang` » ᴛᴏ ᴋᴀɴɢ ᴀɴʏ ᴍɪᴅᴇᴀ..!!

๏ `{hl}getsticker` » ᴛᴏ ɢᴇᴛ ᴀɴʏ sᴛɪᴄᴋᴇʀ ɪɴ ᴘɪᴄ..!!
"""

CRT_MSG = f"""
**ᴄʀᴇᴀᴛᴇ ʜᴇʟᴘ ᴍᴇɴᴜ**

๏ `{hl}create` » ᴛᴏ ᴄʀᴇᴀᴛᴇ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ..!!

๏ `{hl}eflirt` » to impress your crush..!!

๏ `{hl}hflirt` » to impress your crush..!!
"""
SPAM_MSG = f"""
**sᴘᴀᴍ ʜᴇʟᴘ ᴍᴇɴᴜ**

๏ `{hl}spam` » ᴛᴏ sᴘᴀᴍ ᴀɴʏ ᴍᴇssᴀɢᴇ..!!

๏ `{hl}fastspam` » ᴛᴏ sᴘᴀᴍ ᴛᴇxᴛ ғᴀsᴛʟʏ..!!

๏ `{hl}slowspam` » ᴛᴏ sᴘᴀᴍ ᴛᴇxᴛ sʟᴏᴡʟʏ..!!

๏ `{hl}sspam` » ᴛᴏ sᴘᴀᴍ sᴛɪᴄᴋᴇʀs..!!
"""

VC_MSG = f"""
**ᴠᴄ ʜᴇʟᴘ ᴍᴇɴᴜ**

๏ `{hl}startvc` » ᴛᴏ sᴛᴀʀᴛ ᴛʜᴇ ɢᴄ ᴠᴄ..!!

"""

ACC_MSG = f"""
**ᴀᴄᴄᴏᴜɴᴛ ʜᴇʟᴘ ᴍᴇɴᴜ** 

๏ `{hl}setpfp` » sᴇᴛ ᴘғᴘ ᴏғ ᴀᴄᴄ..!!

๏ `{hl}block` » ʙʟᴏᴄᴋ ᴀɴʏ ᴜsᴇʀ..!!

๏ `{hl}unblock` » ᴜɴʙʟᴏᴄᴋ ᴀɴʏ ᴜsᴇʀ..!!

๏ `{hl}setname` » sᴇᴛ ɴᴀᴍᴇ ᴏғ ᴀᴄᴄᴏᴜɴᴛ..!!

๏ `{hl}setbio` » sᴇᴛ ᴘғᴘ ᴏғ ᴀᴄᴄ..!!
"""

ID_MSG = f"""
**ɪᴅs ʜᴇʟᴘ ᴍᴇɴᴜ**

๏ `{hl}Id` » ᴛᴏ ɢᴇᴛ ᴄʜᴀᴛ & ᴜsᴇʀ ɪᴅ..!!
"""

SG_MSG = f"""
**sᴀɴɢᴍᴀᴛᴀ ʜᴇʟᴘ ᴍᴇɴᴜ** 

๏ `{hl}sg` » ᴛᴏ ᴄʜᴇᴄᴋ ᴀɴʏᴏɴᴇ ɴᴀᴍᴇ ʜɪsᴛᴏʀʏ..!!
"""

RAID_MSG = f"""
**ʀᴀɪᴅ ʜᴇʟᴘ ᴍᴇɴᴜ **

๏ `{hl}raid` » ᴛᴏ ʀᴀɪᴅ ᴀɴʏᴏɴᴇ..!!

๏ `{hl}replyraid` » to activate replyraid on user..!!

๏ `{hl}dreplyraid` » to deactivate replyraid on user..!!

๏ `{hl}banall` » to ban all the current chat members..!!
"""

GIT_MSG = f"""
**ɢɪᴛʜᴜʙ ʜᴇʟᴘ ᴍᴇɴᴜ**

๏ `{hl}gitinfo` » ᴛᴏ ɢᴇᴛ ɪɴғᴏ ᴏғ ɢɪᴛ ᴀᴄᴄ..!!
"""

TW_MSG = f"""
**ᴛᴡ ʜᴇʟᴘ ᴍᴇɴᴜ **

๏ `{hl}trump` » ᴛᴏ ᴛʀᴜᴍᴘ ᴛᴡᴇᴇᴛ..!!

๏ `{hl}utweet` » ᴛᴏ ᴛʀᴜᴍᴘ ʙʏ ᴜsᴇʀɴᴀᴍᴇ..!!
"""

FAKE_MSG = f"""
**ғᴀᴋᴇ ʜᴇʟᴘ ᴍᴇɴᴜ**

๏ {hl}f<action> » ʟɪᴋᴇ ᴛʏᴘɪɴɢ > `{hl}ftyping`

ᴜ ᴄᴀɴ ᴜsᴇ ᴅᴏᴄᴜᴍᴇɴᴛ ʟᴏᴄᴀᴛɪᴏɴ ᴇᴛᴄ..!!

๏ `{hl}stupid` » only for fun..!!

๏ `{hl}muth` » only for fun..!!

๏ `{hl}lover` » only for fun..!!

๏ `{hl}iloveu` » only for fun..!!

๏ `{hl}dead` » only for fun..!!
"""

HELP_THREE = IKM(
             [
             [
             IKB("ɪᴍᴘᴏʀᴛᴀɴᴛ", callback_data="im"),
             IKB("ᴘᴍ", callback_data="dm")
             ],
             [
             IKB("sᴇᴄʀᴇᴛ", callback_data="sec")
             ],
             [
             IKB("ᴀғᴋ", callback_data="af"),
             IKB("ᴄʀᴇᴀᴛᴇ", callback_data="crt")
             ],
             [
             IKB("sᴛɪᴄᴋᴇʀ", callback_data="stk")
             ],
             [
             IKB("🏡", callback_data="home")
             ]
             ]
             )

HELP_TWO = IKM(
           [
           [
           IKB("ᴀᴄᴄᴏᴜɴᴛ", callback_data="acc"),
           IKB("ɪᴅs", callback_data="id")
           ],
           [
           IKB("sᴀɴɢᴍᴀᴛᴀ", callback_data="sg")
           ],
           [
           IKB("ʀᴀɪᴅ", callback_data="rd"),
           IKB("ᴛᴡᴇᴇᴛ", callback_data="tw")
           ],
           [
           IKB("ғᴀᴋᴇ", callback_data="fk")
           ],
           [
           IKB("🏡", callback_data="home")
           ]
           ]
           )

HELP_MARKUP = IKM(
              [
              [
              IKB("ᴀᴅᴍɪɴs", callback_data="admin"),
              IKB("ᴇxᴛʀᴀ", callback_data="exa")
              ],
              [
              IKB("ɪɴᴠɪᴛᴇ", callback_data="inv")
              ],
              [
              IKB("sᴘᴀᴍ", callback_data="pam"),
              IKB("ᴠᴄ", callback_data="v")
              ],
              [
             IKB("ɢɪᴛʜᴜʙ", callback_data="git")
              ],
              [
              IKB("⬅️", callback_data="left"),
              IKB("➡️", callback_data="right")
              ]
              ]
              )
sux = None

BACK = IKM(
       [
       [
       IKB("🔙", callback_data="back")
       ]
       ]
       )

BACKK = IKM(
       [
       [
       IKB("🔙", callback_data="backk")
       ]
       ]
       ) 

BACKKK = IKM(
       [
       [
       IKB("🔙", callback_data="backkk")
       ]
       ]
       ) 

@RBX.on_message(filters.command("help", hl))
async def help(client, message):
    global sux
    if not sux:
        sux = (await bot.get_me()).username
    await message.edit("`ɢᴇᴛᴛɪɴɢ ʜᴇʟᴘ ᴍᴇɴᴜ...!!`")
    try:
        nice = await client.get_inline_bot_results(bot=sux, query="inline_help")
    except Exception as e:
        return await message.reply(e)
    try:
        await message.delete()
        await message.delete()
    except:
        pass
    try:
        await client.send_inline_bot_result(message.chat.id, nice.query_id, nice.results[0].id)
    except Exception as e:
        await message.reply(e)

ans = [IQRP(photo_url=HELP_PIC, thumb_url=PIC, title="Help", description="Help Menu", caption=HELP_TEXT, reply_markup=HELP_MARKUP)]

@bot.on_inline_query()
async def inl(y, x):
    text = x.query.lower()
    try:
        if text == "inline_help":
            await y.answer_inline_query(x.id, results=ans, cache_time=0)     
    except Exception as e:
        print(e)

@bot.on_callback_query(filters.regex("back"))
async def admin(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=HELP_TEXT, reply_markup=HELP_MARKUP)
  
@bot.on_callback_query(filters.regex("admin"))
async def admin(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=ADMINS_MSG, reply_markup=BACK)

@bot.on_callback_query(filters.regex("exa"))
async def extra(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=EXTRA_MSG, reply_markup=BACK)

@bot.on_callback_query(filters.regex("inv"))
async def invite(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=INVITE_MSG, reply_markup=BACK)

@bot.on_callback_query(filters.regex("pam"))
async def spam(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=SPAM_MSG, reply_markup=BACK)

@bot.on_callback_query(filters.regex("v"))
async def vc(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=VC_MSG, reply_markup=BACK)

@bot.on_callback_query(filters.regex("git"))
async def git(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=GIT_MSG, reply_markup=BACK)

@bot.on_callback_query(filters.regex("close"))
async def close(client, r):
    if r.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await r.answer()
    await r.message.delete()

@bot.on_callback_query(filters.regex("left"))
async def left(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=HELP_TEXT2, reply_markup=HELP_TWO)

@bot.on_callback_query(filters.regex("right"))
async def left(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=HELP_TEXT3, reply_markup=HELP_THREE)
           
@bot.on_callback_query(filters.regex("home"))
async def home(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=HELP_TEXT, reply_markup=HELP_MARKUP)

@bot.on_callback_query(filters.regex("backk"))
async def admin(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=HELP_TEXT2, reply_markup=HELP_TWO)

@bot.on_callback_query(filters.regex("backkk"))
async def admin(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=HELP_TEXT3, reply_markup=HELP_THREE)

@bot.on_callback_query(filters.regex("acc"))
async def acc(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=ACC_MSG, reply_markup=BACKK)

@bot.on_callback_query(filters.regex("id"))
async def id(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=ID_MSG, reply_markup=BACKK)

@bot.on_callback_query(filters.regex("sg"))
async def sg(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=SG_MSG, reply_markup=BACKK)

@bot.on_callback_query(filters.regex("rd"))
async def rd(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=RAID_MSG, reply_markup=BACKK)

@bot.on_callback_query(filters.regex("tw"))
async def tw(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=TW_MSG, reply_markup=BACKK)

@bot.on_callback_query(filters.regex("fk"))
async def fk(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=FAKE_MSG, reply_markup=BACKK)

@bot.on_callback_query(filters.regex("im"))
async def rd(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=IMPORT_MSG, reply_markup=BACKKK)

@bot.on_callback_query(filters.regex("dm"))
async def rd(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=DM_MSG, reply_markup=BACKKK)

@bot.on_callback_query(filters.regex("sec"))
async def rd(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=SEC_MSG, reply_markup=BACKKK)

@bot.on_callback_query(filters.regex("af"))
async def rd(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=AFK_MSG, reply_markup=BACKKK)

@bot.on_callback_query(filters.regex("crt"))
async def rd(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=CRT_MSG, reply_markup=BACKKK)

@bot.on_callback_query(filters.regex("stk"))
async def rd(client, message):
    if message.from_user.id != RBX.me.id:
        return await message.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=STK_MSG, reply_markup=BACKKK)
