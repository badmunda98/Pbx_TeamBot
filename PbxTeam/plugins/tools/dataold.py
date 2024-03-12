import asyncio
from pyrogram import *
from pyrogram import filters
from pyrogram.types import *
from pyrogram import Client
from pyrogram.errors import RPCError
from ... import app, SUDO_USER
from ... import *
from PbxTeam.modules.bad.basic import edit_or_reply

@app.on_message(cdz(["oldname"])  & (filters.me | filters.user(SUDO_USER)))
async def user_history(app: app, message: Message):
    lol = await edit_or_reply(message, "Processing please wait")
    if not message.reply_to_message:
        await lol.edit("reply to any message")
    reply = message.reply_to_message
    if not reply.text:
        await lol.edit("reply to any text message")
    chat = message.chat.id
    try:
        await app.send_message("@SangMataInfo_bot", "/start")
    except RPCError:
        await lol.edit("Please unblock @SangMataInfo_bot and try again")
        return
    await reply.forward("@SangMataInfo_bot")
    await asyncio.sleep(2)
    async for opt in client.iter_history("@SangMataInfo_bot", limit=3):
        hmm = opt.text
        if hmm.startswith("Forward"):
            await lol.edit("Can you kindly disable your privacy settings for good")
            return
        else:
            await lol.delete()
            await opt.copy(chat)




