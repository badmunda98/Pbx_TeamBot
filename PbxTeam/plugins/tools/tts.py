from pyrogram import Client, filters
from gtts import gTTS
from ... import *
from ... import app, SUDO_USER

@app.on_message(
    filters.command(["tts"], ".") & (filters.me | filters.user(SUDO_USER))
)
def text_to_speech(client, message):
    text = message.text.split(' ', 1)[1]
    tts = gTTS(text=text, lang='hi')
    tts.save('ᴮᴬᴰ ᴬᵁᴰᴵᴼ.mp3')
    client.send_audio(message.chat.id, 'ᴮᴬᴰ ᴬᵁᴰᴵᴼ.mp3')
  

__NAME__ = "tts"
__MENU__ = """
`.tts` - **text to speech .**

"""
