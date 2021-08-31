import asyncio

from uniborg.util import admin_cmd
from userbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Happy BirthDay Diiiii"
 #credit - @weTemp

@borg.on(admin_cmd(pattern=r"dear "))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2.0

    animation_ttl = range(0, 50)

    await event.edit("🤩")

    animation_chars = [
    "Dear Didi💜",
"On The Special Day of Your Life🤩",
"I pray With the God That🙏",
"Meri Behen ko Har wo Chiz Mile❤️",
"Jo Bhi She wants To Achieve🥰",
"NEET Crack Kar le behen Meri...😍"
"Wo Always Happy Rhe😊",
"Wishing You🥳",
"A Very Very Happy Birthday....🥰🥳🤩😘",
"To My Dear Behen...:)❤️❤️😘",
"May all Her Dreams come True....🤩🥰",
"Happy BirthDay Meri Behen...😊❤️"
   
     
   ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 50])