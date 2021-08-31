from .. import Legend, Legend2, Legend3, Legend4, Legend5, Legend6, Legend7, Legend8, Legend9, Legend10, SUDO_USERS
from telethon import events
import os
import random
import sys

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

@Legend.on(events.NewMessage(pattern="/restart"))
@Legend2.on(events.NewMessage(pattern="/restart"))
@Legend3.on(events.NewMessage(pattern="/restart"))
@Legend4.on(events.NewMessage(pattern="/restart"))
@Legend5.on(events.NewMessage(pattern="/restart"))
@Legend6.on(events.NewMessage(pattern="/restart"))
@Legend7.on(events.NewMessage(pattern="/restart"))
@Legend8.on(events.NewMessage(pattern="/restart"))
@Legend9.on(events.NewMessage(pattern="/restart"))
@Legend10.on(events.NewMessage(pattern="/restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = " 🤷‍♂️𝐑𝐄𝐒𝐓𝐀𝐑𝐓𝐄𝐃🤧\n🔰𝐏𝐋𝐄𝐀𝐒𝐄 𝐖𝐀𝐈𝐓 𝐓𝐈𝐋𝐋 𝐈𝐓 𝐑𝐄𝐁𝐎𝐎𝐓𝐒....\n👉Made By 「 ᴴᶦᵐ」🇮🇳 "
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await Legend.disconnect()
        except Exception:
            pass
        try:
            await Legend2.disconnect()
        except Exception:
            pass
        try:
            await Legend3.disconnect()
        except Exception:
            pass
        try:
            await Legend4.disconnect()
        except Exception:
            pass
        try:
            await Legend5.disconnect()
        except Exception:
            pass
        try:
            await Legend6.disconnect()
        except Exception:
            pass
        try:
            await Legend7.disconnect()
        except Exception:
            pass
        try:
            await Legend8.disconnect()
        except Exception:
            pass
        try:
            await Legend9.disconnect()
        except Exception:
            pass
        try:
            await Legend10.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
