import os
import sys
import asyncio
from time import time
from datetime import datetime
from pyrogram import __version__, filters, Client
from pyrogram.types import Message
from platform import python_version
from ... import app, SUDO_USER
from ... import *

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@app.on_message(cdz(["alive"])  & (filters.me | filters.user(SUDO_USER)))
async def alive(client: Client, message: Message):
    r = await message.reply_text("**𝐀𝐋𝐈𝐕𝐄**")
    start = time()
    current_time = datetime.utcnow()
    ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.delete()
    await r.edit(
        f"❥︎ 𝐀𝐋𝐈𝐕𝐄 ☟︎︎︎\n\n"
        f"ᴠᴇʀsɪᴏɴ★ 1.0\n"
        f"ᴘɪɴɢ ★ {ping * 1000:.3f}ᴍs\n"
        f"ᴜᴘ ★ᴛɪᴍᴇ ★ {uptime}\n"
        f"ᴘʏᴛʜᴏɴ ★ {python_version()}`\n"
        f"ᴘʏʀᴏɢʀᴀᴍ ★ {__version__}\n"
        f"ᴏᴡɴᴇʀ ★ {client.me.mention}"    
    )

@app.on_message(cdz(["ping"])  & (filters.me | filters.user(SUDO_USER)))
async def ping(client: Client, message: Message):
    r = await message.reply_text("**𝐏𝐎𝐍𝐆**")
    start = time()
    current_time = datetime.utcnow()
    ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.delete()
    await r.edit(
        f"★ 𝗣𝗢𝗡𝗚 ★\n\n"
        f"ᴘɪɴɢ ★ {ping * 1000:.3f}ᴍs\n"
        f"ᴜᴘ ★ ᴛɪᴍᴇ ★ {uptime}\n"
        f"ᴏᴡɴᴇʀ ★ {client.me.mention}\n"
              )
@app.on_message(cdz(["repo"])  & (filters.me | filters.user(SUDO_USER)))
async def ping(client: Client, message: Message):
    r = await message.reply_text("**𝐑𝐄𝐏𝐎 ❥︎**")
    start = time()
    current_time = datetime.utcnow()
    ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.delete()
    await r.edit(
        f"𝐑𝐄𝐏𝐎 ❥︎★\n\n"
        f"[💫 𝐑ᴇᴘᴏ 💫](https://github.com/Badhacker98/Pbx_TeamBot/fork)\n"
    )    

@app.on_message(cdz(["allrepo"])  & (filters.me | filters.user(SUDO_USER)))
async def ping(client: Client, message: Message):
    r = await message.reply_text("**𝐀𝐋𝐋 𝐑𝐄𝐏𝐎 ❥︎**")
    start = time()
    current_time = datetime.utcnow()
    ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.delete()
    await r.edit(
        f"𝐀𝐋𝐋 𝐑𝐄𝐏𝐎 ❥︎★\n\n"
        f"[💫𝐀ʟʟ 𝐑ᴇᴘᴏ 💫](https://github.com/Badhacker98?tab=repositories)\n"
    )    


__NAME__ = "ᴀᴄᴛɪᴠᴇ"
__MENU__ = """
`.ping` - **Check Ping Latency
Of Your Userbot Server.**

`.alive` - **Check Ping Latency
Of Your Userbot Server.**

`.repo` - **chek bot repo.**
`.allrepo` - **chek bot repo.**
"""
