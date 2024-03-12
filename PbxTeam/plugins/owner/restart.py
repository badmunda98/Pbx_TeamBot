import os
import shutil
import asyncio
from pyrogram.types import Message
from pyrogram import filters, Client
from ... import app, SUDO_USER
from ... import *

@app.on_message(cdz(["restart"]) & (filters.me | filters.user(SUDO_USER)))
async def restart(client: Client, message: Message):
    reply = await message.reply_text("**🔁 Rᴇsᴛᴀʀᴛɪɴɢ 🔥 ...**")
    await message.delete()
    await reply.edit_text("🥀 SᴜᴄᴄᴇssFᴜʟʟʏ RᴇSᴛᴀʀᴛᴇᴅ\n ᴘʙx シ︎ UsᴇʀBᴏᴛ 🔥 ...\n\n💕 Pʟᴇᴀsᴇ Wᴀɪᴛ 1-2 MɪN Fᴏʀ\nLᴏᴀᴅ Usᴇʀ Pʟᴜɢɪɴs ✨ ...</b>")
    os.system(f"kill -9 {os.getpid()} && python3 -m PbxTeam")
  

__NAME__ = "ʀᴇsᴛᴀʀᴛ"
__MENU__ = """
`.restart` **heroku bot restart **
`.upload` **Upload the file to telegram from the given system file path**
"""
