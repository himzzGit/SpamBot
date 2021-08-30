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



@Legend.on(events.NewMessage(pattern=".bigspam"))
@Legend2.on(events.NewMessage(pattern=".bigspam"))
@Legend3.on(events.NewMessage(pattern=".bigspam"))
@Legend4.on(events.NewMessage(pattern=".bigspam"))
@Legend5.on(events.NewMessage(pattern=".bigspam"))
@Legend6.on(events.NewMessage(pattern=".bigspam"))
@Legend7.on(events.NewMessage(pattern=".bigspam"))
@Legend8.on(events.NewMessage(pattern=".bigspam"))
@Legend9.on(events.NewMessage(pattern=".bigspam"))
@Legend10.on(events.NewMessage(pattern=".bigspam"))
async def spam(e):
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Legend = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Legend) == 2:
            message = str(Legend[1])
            counter = int(Legend[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.media:
            counter = int(Legend[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Legend[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
