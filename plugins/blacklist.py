# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}blacklist <word/all words with a space>`
    blacklist the choosen word in that chat.

• `{i}remblacklist <word>`
    Remove the word from blacklist..

• `{i}listblacklist`
    list all blacklisted words.

  'if a person uses blacklist Word his/her msg will be deleted'
  'And u Must be Admin in that Chat'
"""

import re

from pyUltroid.functions.blacklist_db import *
from telethon.tl.types import ChannelParticipantsAdmins

from . import *


@ultroid_cmd(pattern="blacklist ?(.*)")
async def af(e):
    wrd = (e.pattern_match.group(1)).lower()
    chat = e.chat_id
    if not (wrd):
        return await eod(e, "`Give the word to blacklist..`")
    wrd = e.text[10:]
    add_blacklist(int(chat), wrd)
    await eor(e, f"Done : `{wrd}` Blacklisted here.")


@ultroid_cmd(pattern="remblacklist ?(.*)")
async def rf(e):
    wrd = (e.pattern_match.group(1)).lower()
    chat = e.chat_id
    if not wrd:
        return await eod(e, "`Give the word to remove from blacklist..`")
    rem_blacklist(int(chat), wrd)
    await eor(e, f"Done : `{wrd}` Removed from Blacklist.")


@ultroid_cmd(pattern="listblacklist")
async def lsnote(e):
    x = list_blacklist(e.chat_id)
    if x:
        sd = "Blacklist Found In This Chats Are\n\n"
        await eor(e, sd + x)
    else:
        await eor(e, "No Blacklist word Found Here")


@ultroid_bot.on(events.NewMessage(incoming=True))
async def bl(e):
    chat = e.chat_id
    x = get_blacklist(int(chat))
        if " " in xx:
            xx = xx.split(" ")
            kk = ""
            for c in xx:
                kk = re.search(str(c), str(x), flags=re.IGNORECASE)
            if kk:
                try:
                    await e.delete()
        else:
            k = re.search(xx, x, flags=re.IGNORECASE)
            if k:
                try:
                    await e.delete()


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
