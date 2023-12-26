from config import HANDLER as hl
from Subhi.userbot import RBX
from pyrogram import Client, filters, enums
from gtts import gTTS


def convert(txt):
    tts = gTTS(txt)
    x = "Subhi.mp3"
    tts.save(x)
    return x

@RBX.on_message(filters.command("tts", hl) & filters.me)
async def teeteeyess(_, m):
    reply = m.reply_to_message
    if not reply:
        if len(m.command) < 2:
            return await eor(m, "**Either reply or give some text..!!**")
    
    if reply:
        if not reply.text and not reply.caption:
            return await eor(m, "**No text found in replied messages.!!**")
        txt = reply.text if reply.text else reply.caption
        path = convert(txt)
    else:
        txt = m.text.split(None, 1)[1]
        path = convert(txt)
    try:
        await m.delete()
    except:
        pass
    try:
        await _.send_chat_action(m.chat.id, enums.ChatAction.RECORD_AUDIO)
        await m.reply_voice(path)
        await _.send_chat_action(m.chat.id, enums.ChatAction.CANCEL)
    except:
        await _.send_chat_action(m.chat.id, enums.ChatAction.RECORD_AUDIO)
        await m.reply_audio(path)
        await _.send_chat_action(m.chat.id, enums.ChatAction.CANCEL)
