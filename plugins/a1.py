# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available
🔹 `{i}shift <from channel> | <to channel>`
     This will transfer all old post from channel A to channel B.
      (u can use username or id of channel too)
      example : `{i}shift @abc | @xyz`
      [note - this (" | ") sign is nessesary]
🔹 For auto-posting/forwarding all new message from any source channel to any destination channel.
   * `asource <channel username or id>`
      This add source channel to database
   * `dsource <channel username or id>`
      This remove source channels from database
   * `listsource <channel username or id>`
      Show list of source channels
   * `{i}adest <channel username or id>`
      This add Ur channels to database
   * `{i}ddest <channel username or id>`
      This Remove Ur channels from database
   * `{i}listdest <channel username or id>`
      Show List of Ur channels
   'you can set many channels in database'
   'For activating auto-post use `{i}setredis AUTOPOST True` '
"""

import asyncio

from pyUltroid.functions.ch_db import *

from . import *


@ultroid_bot.on(events.NewMessage())
async def _(e):
    if not udB.get("AUTOPOST") == "True":
        return
    s = get_source_channels()
    ch = await e.get_chat()
    for cs in s:
        if str(ch.id) not in str(cs):
            return
    m = get_destinations()
    for ks in m:
        try:
            if e.text and not e.media:
                await ultroid_bot.send_message(int(ks), e.text)
            elif e.media and e.text:
                await ultroid_bot.send_file(int(ks), e.media, caption=e.text)
            else:
                await ultroid_bot.send_file(int(ks), e.media)
        except Exception as e:
            await ultroid_bot.send_message(bot.me.id, str(e))



@ultroid_cmd(pattern="c1source (.*)")
async def source(e):
    j = e.pattern_match.group(1)
    try:
        q = int(j)
    except Exception:
        try:
            q = int((await bot.get_entity(j)).id)
        except Exception as es:
            print(es)
            return
    if not is_source_channel_added(q):
        add_source_channel(q)
        await eor(e, "Source added succesfully")
    elif is_source_channel_added(q):
        await eor(e, "Source channel already added")



@ultroid_cmd(pattern="c1dest (.*)")
async def destination(e):
    j = e.pattern_match.group(1)
    try:
        q = int(j)
    except Exception:
        try:
            q = int((await bot.get_entity(j)).id)
        except Exception as es:
            print(es)
            return
    if not is_destination_added(q):
        add_destination(q)
        await eor(e, "Destination added succesfully")
    elif is_destination_added(q):
        await eor(e, "Destination channel already added")


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
