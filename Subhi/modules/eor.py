async def eor(shiva, riyu):
    try:
        return await shiva.edit(riyu)
    except:
        return await shiva.reply(riyu)
