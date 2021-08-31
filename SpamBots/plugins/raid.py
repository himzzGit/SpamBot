
import asyncio
import base64
import os
import random
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import  Legend, Legend2, Legend3, Legend4, Legend5, Legend6, Legend7, Legend8, Legend9, Legend10, SUDO_USERS
SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

que = {}



@Legend.on(events.NewMessage(pattern=".raid"))
@Legend2.on(events.NewMessage(pattern=".raid"))
@Legend3.on(events.NewMessage(pattern=".raid"))
@Legend4.on(events.NewMessage(pattern=".raid"))
@Legend5.on(events.NewMessage(pattern=".raid"))
@Legend6.on(events.NewMessage(pattern=".raid"))
@Legend7.on(events.NewMessage(pattern=".raid"))
@Legend8.on(events.NewMessage(pattern=".raid"))
@Legend9.on(events.NewMessage(pattern=".raid"))
@Legend10.on(events.NewMessage(pattern=".raid"))
async def spam(e):  
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Legend = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Legend) == 2:
            message = str(Legend[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(Legend[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(Legend[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



@Legend.on(events.NewMessage(incoming=True))
@Legend2.on(events.NewMessage(incoming=True))
@Legend3.on(events.NewMessage(incoming=True))
@Legend4.on(events.NewMessage(incoming=True))
@Legend5.on(events.NewMessage(incoming=True))
@Legend6.on(events.NewMessage(incoming=True))
@Legend7.on(events.NewMessage(incoming=True))
@Legend8.on(events.NewMessage(incoming=True))
@Legend9.on(events.NewMessage(incoming=True))
@Legend10.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )


@Legend.on(events.NewMessage(pattern="/replyraid"))
@Legend2.on(events.NewMessage(pattern="/replyraid"))
@Legend3.on(events.NewMessage(pattern="/replyraid"))
@Legend4.on(events.NewMessage(pattern="/replyraid"))
@Legend5.on(events.NewMessage(pattern="/replyraid"))
@Legend6.on(events.NewMessage(pattern="/replyraid"))
@Legend7.on(events.NewMessage(pattern="/replyraid"))
@Legend8.on(events.NewMessage(pattern="/replyraid"))
@Legend9.on(events.NewMessage(pattern="/replyraid"))
@Legend10.on(events.NewMessage(pattern="/replyraid"))
async def _(e):
    global que
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Ustad = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(e.text) > 11:
            message = str(Legend[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None)
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)

@Legend.on(events.NewMessage(pattern=".drraid"))
@Legend2.on(events.NewMessage(pattern=".drraid"))
@Legend3.on(events.NewMessage(pattern=".drraid"))
@Legend4.on(events.NewMessage(pattern=".drraid"))
@Legend5.on(events.NewMessage(pattern=".drraid"))
@Legend6.on(events.NewMessage(pattern=".drraid"))
@Legend7.on(events.NewMessage(pattern=".drraid"))
@Legend8.on(events.NewMessage(pattern=".drraid"))
@Legend9.on(events.NewMessage(pattern=".drraid"))
@Legend10.on(events.NewMessage(pattern=".drraid"))
async def _(e):
    global que    
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Legend = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Legend[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
