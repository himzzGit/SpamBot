async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import Legend, Legend2, Legend3, Legend4, Legend5, Legend6, Legend7, Legend8, Legend9, Legend10, SUDO_USERS

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)



@Legend.on(events.NewMessage(pattern=".spam"))
@Legend2.on(events.NewMessage(pattern=".spam"))
@Legend3.on(events.NewMessage(pattern=".spam"))
@Legend4.on(events.NewMessage(pattern=".spam"))
@Legend5.on(events.NewMessage(pattern=".spam"))
@Legend6.on(events.NewMessage(pattern=".spam"))
@Legend7.on(events.NewMessage(pattern=".spam"))
@Legend8.on(events.NewMessage(pattern=".spam"))
@Legend9.on(events.NewMessage(pattern=".spam"))
@Legend10.on(events.NewMessage(pattern=".spam"))
async def spam(e):
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Legend = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Legend) == 2:
            message = str(Legend[1])
            counter = int(Legend[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(Legend[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Legend[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
