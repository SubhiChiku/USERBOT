import asyncio

from pyrogram import Client, __version__ as ver

API_ID = input("\nEnter Your API ID \n > ")
API_HASH = input("\nEnter Your API HASH \n > ")

print("\n\nEnter the phone number\n\n")

rabbit = Client("bunny", api_id=API_ID, api_hash=API_HASH, in_memory=True)


async def main():
    await rabbit.start()
    sex = await rabbit.export_session_string()
    fuk = f"Here is your Pyrogram {ver} String Session\n\n<code>{sex}</code>\n\nDon't share it with anyone.\nDon't forget to join @SUBI_WORLD"
    ok = await rabbit.send_message("me", fuk)
    print(f"go to your saved message and enjoy 🔥🔥") 

asyncio.run(main())
