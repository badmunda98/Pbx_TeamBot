from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from ... import *

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command(["r", "repo"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3063af27d9cc8580845e1.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️

[💫 𝐑ᴇᴘᴏ 💫](https://github.com/Badhacker98/Pbx_TeamBot/fork)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ ᴘʙx ᴛᴇᴀᴍ ʀᴇᴘᴏ 🗡️", url=f"https://github.com/Badhacker98/Pbx_TeamBot/fork")
                ],

            ]
        ),
    )

@app.on_message(
    filters.command(["r", "repo"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3063af27d9cc8580845e1.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️

[💫 𝐑ᴇᴘᴏ 💫](https://github.com/Badhacker98/Pbx_TeamBot/fork)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ ᴘʙx ᴛᴇᴀᴍ ʀᴇᴘᴏ 🗡️", url=f"https://github.com/Badhacker98/Pbx_TeamBot/fork")
                ],

            ]
        ),
    )

@app.on_message(
    filters.command(["repo", "repo"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3063af27d9cc8580845e1.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️

[💫 𝐑ᴇᴘᴏ 💫](https://github.com/Badhacker98/Pbx_TeamBot/fork)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ ᴘʙx ᴛᴇᴀᴍ ʀᴇᴘᴏ 🗡️", url=f"https://github.com/Badhacker98/Pbx_TeamBot/fork")
                ],

            ]
        ),
        )


__NAME__ = "repo"
__MENU__ = """
`.repo` - **chek bot repo.**

"""
