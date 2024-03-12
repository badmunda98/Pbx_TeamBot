import asyncio
from pyrogram import Client, filters 
from pyrogram.types import Message
from ... import app, SUDO_USER
from ... import *
from PbxTeam.modules.bad.basics import edit_or_reply
from PbxTeam.modules.bad.command import commandpro

@app.on_message(cdz(["adduser"])  & (filters.me | filters.user(SUDO_USER))
)
async def inviteall(client: Client, message: Message):
    kaal = await edit_or_reply(message, "Processing ...")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await client.get_chat(queryy)
    tgchat = message.chat
    await kaal.edit_text(f"**🥀 Iɴᴠɪᴛɪɴɢ Usᴇʀs Fʀᴏᴍ {chat.username} ✨ ...**")
    async for member in client.iter_chat_members(chat.id):
        user= member.user
        kal= ["online", "offline" , "recently", "within_week"]
        if user.status in kal:
           try:
            await client.add_chat_members(tgchat.id, user.id)
           except Exception as e:
            mg= await client.send_message("me", f"error-   {e}")
            await asyncio.sleep(0.3)
            await mg.delete()



