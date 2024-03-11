import asyncio
import random
import asyncio
from random import choice
import time
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import filters, Client
from PbxTeam.modules.bad.data import PBRAID
from PbxTeam.modules.bad.data import * 
from ... import app, SUDO_USER
from ... import *

@app.on_message(cdz(["pbiraid"])  & (filters.me | filters.user(SUDO_USER))
)
async def pbiraid(app: Client, m: Message):  
      PbxTeam = "".join(m.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(PbxTeam) == 2:
        counts = int(PbxTeam[0])
        username = PbxTeam[1]
        if not counts:
          await m.reply_text(f"PBIRAID LIMIT NOT FOUND PLEASE GIVE COUNT!")
          return       
        if not username:
          await m.reply_text("you need to specify an user! Reply to any user or gime id/username")
          return
        try:
           user = await app.get_users(Romeo[1])
        except:
           await m.reply_text("**Error:** User not found or may be deleted!")
           return
      elif m.reply_to_message:
        counts = int(PbxTeam[0])
        try:
           user = await app.get_users(m.reply_to_message.from_user.id)
        except:
           user = m.reply_to_message.from_user 
      else:
        await m.reply_text("Usage: .pbiraid count username or reply")
        return
      if int(m.chat.id) in GROUP:
         await m.reply_text("**Sorry !! i Can't Spam Here.**")
         return
      if int(user.id) in VERIFIED_USERS:
         await m.reply_text("I can't raid on my developer")
         return
      if int(user.id) in SUDO_USER:
         await m.reply_text("This guy is a sudo users.")
         return
      mention = user.mention
      for _ in range(counts): 
         r = f"{mention} {choice(PBRAID)}"
         await app.send_message(m.chat.id, r)
         await asyncio.sleep(0.3)

#........................................#

@app.on_message(cdz(["dmpbiraid"])  & (filters.me | filters.user(SUDO_USER))
)
async def dmpbiraid(app: Client, m: Message):  
      PbxTeam = "".join(m.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(PbxTeam) == 2:
        counts = int(PbxTeam[0])
        username = PbxTeam[1]
        if not counts:
          await m.reply_text(f"DMPBIRAID LIMIT NOT FOUND PLEASE GIVE COUNT!")
          return       
        if not username:
          await m.reply_text("you need to specify an user! Reply to any user or gime id/username")
          return
        try:
           user = await app.get_users(PbxTeam[1])
        except:
           await m.reply_text("**Error:** User not found or may be deleted!")
           return
      elif m.reply_to_message:
        counts = int(PbxTeam[0])
        try:
           user = await app.get_users(m.reply_to_message.from_user.id)
        except:
           user = m.reply_to_message.from_user 
      else:
        await m.reply_text("Usage: .dmpbbiraid count username or reply")
        return
      if int(user.id) in VERIFIED_USERS:
         await m.reply_text("I can't Pbiraid on my developer")
         return
      if int(user.id) in SUDO_USER:
         await m.reply_text("This guy is a sudo users.")
         return
      mention = user.mention
      await m.reply_text("Dm Pbiaid started..")
      for _ in range(counts): 
         r = f"{choice(PBRAID)}"
         await app.send_message(user.id, r)
         await asyncio.sleep(0.3)
