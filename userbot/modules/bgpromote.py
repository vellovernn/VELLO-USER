# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
"""
✘ Commands Available -



•`{i}bgpromote <reply to user> <channel/group/all> <rank>`
    globally promote user where you are admin.
    You can also set where To promote only groups or only channels or in all.
    Like. `gpromote group boss` ~ it promote repied user in all groups.
    Or. `gpromote @username all sar` ~ it promote the users in all group and channel.

•`{i}bgdemote`
    Same function as gpromote.
"""
import os

from pyUltroid.functions.gban_mute_db import *
from pyUltroid.functions.gcast_blacklist_db import *
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import ChatAdminRights

from . import *

_gpromote_rights = ChatAdminRights(
    add_admins=True,
    invite_users=True,
    change_info=True,
    ban_users=True,
    delete_messages=True,
    pin_messages=True,
    manage_call=True,
    
)

_gdemote_rights = ChatAdminRights(
    add_admins=False,
    invite_users=False,
    change_info=False,
    ban_users=False,
    delete_messages=False,
    pin_messages=False,
    manage_call=False,
    
)


@ultroid_cmd(
    pattern="bgpromote ?(.*)",
)
async def _(e):
    if not e.out and not is_fullsudo(e.sender_id):
        return await eod(e, "`This Command Is Sudo Restricted.`")
    x = e.pattern_match.group(1)
    ultroid_bot = e.client
    if not x:
        return await eod(e, "`Incorrect Format`")
    user = await e.get_reply_message()
    if user:
        ev = await eor(e, "`Promoting Replied User Globally`")
        ok = e.text.split()
        key = "all"
        if len(ok) > 1:
            if ("group" in ok[1]) or ("channel" in ok[1]):
                key = ok[1]
        rank = "AdMin"
        if len(ok) > 2:
            rank = ok[2]
        c = 0
        if e.is_private:
            user.id = user.peer_id.user_id
        else:
            user.id = user.from_id.user_id
        async for x in e.client.iter_dialogs():
            if "group" in key.lower():
                if x.is_group:
                    try:
                        await e.client(
                            EditAdminRequest(
                                x.id,
                                user.id,
                                _gpromote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            elif "channel" in key.lower():
                if x.is_channel:
                    try:
                        await e.client(
                            EditAdminRequest(
                                x.id,
                                user.id,
                                _gpromote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            else:
                if x.is_group or x.is_channel:
                    try:
                        await e.client(
                            EditAdminRequest(
                                x.id,
                                user.id,
                                _gpromote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except Exception as er:
                        LOGS.info(er)
        return await eor(ev, f"Promoted The Replied Users in Total : {c} {key} chats")
    else:
        k = e.text.split()
        if not k[1]:
            return await eod(e, "`Give someone's username/id or replied to user.")
        user = k[1]
        if user.isdigit():
            user = int(user)
        try:
            name = await e.client.get_entity(user)
        except BaseException:
            return await eod(e, f"`No User Found Regarding {user}`")
        ev = await eor(e, f"`Promoting {name.first_name} globally.`")
        key = "all"
        if len(k) > 2:
            if ("group" in k[2]) or ("channel" in k[2]):
                key = k[2]
        rank = "AdMin"
        if len(k) > 3:
            rank = k[3]
        c = 0
        async for x in e.client.iter_dialogs():
            if "group" in key.lower():
                if x.is_group:
                    try:
                        await ultroid_bot(
                            EditAdminRequest(
                                x.id,
                                user,
                                _gpromote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            elif "channel" in key.lower():
                if x.is_channel:
                    try:
                        await ultroid_bot(
                            EditAdminRequest(
                                x.id,
                                user,
                                _gpromote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            else:
                if x.is_group or x.is_channel:
                    try:
                        await ultroid_bot(
                            EditAdminRequest(
                                x.id,
                                user,
                                _gpromote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
        return await eor(ev, f"Promoted {name.first_name} in Total : {c} {key} chats.")


@ultroid_cmd(
    pattern="bgdemote ?(.*)",
)
async def _(e):
    if not e.out and not is_fullsudo(e.sender_id):
        return await eod(e, "`This Command Is Sudo Restricted.`")
    x = e.pattern_match.group(1)
    ultroid_bot = e.client
    if not x:
        return await eod(e, "`Incorrect Format`")
    user = await e.get_reply_message()
    if user:
        if e.is_private:
            user.id = user.peer_id.user_id
        else:
            user.id = user.from_id.user_id
        ev = await eor(e, "`Demoting Replied User Globally`")
        ok = e.text.split()
        key = "all"
        if len(ok) > 1:
            if ("group" in ok[1]) or ("channel" in ok[1]):
                key = ok[1]
        rank = "Not AdMin"
        c = 0
        async for x in e.client.iter_dialogs():
            if "group" in key.lower():
                if x.is_group:
                    try:
                        await ultroid_bot(
                            EditAdminRequest(
                                x.id,
                                user.id,
                                _gdemote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            elif "channel" in key.lower():
                if x.is_channel:
                    try:
                        await ultroid_bot(
                            EditAdminRequest(
                                x.id,
                                user.id,
                                _gdemote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            else:
                if x.is_group or x.is_channel:
                    try:
                        await ultroid_bot(
                            EditAdminRequest(
                                x.id,
                                user.id,
                                _gdemote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
        return await eor(ev, f"Demoted The Replied Users in Total : {c} {key} chats")
    else:
        k = e.text.split()
        if not k[1]:
            return await eod(e, "`Give someone's username/id or replied to user.")
        user = k[1]
        if user.isdigit():
            user = int(user)
        try:
            name = await ultroid_bot.get_entity(user)
        except BaseException:
            return await eod(e, f"`No User Found Regarding {user}`")
        ev = await eor(e, f"`Demoting {name.first_name} globally.`")
        key = "all"
        if len(k) > 2:
            if ("group" in k[2]) or ("channel" in k[2]):
                key = k[2]
        rank = "Not AdMin"
        c = 0
        async for x in ultroid_bot.iter_dialogs():
            if "group" in key.lower():
                if x.is_group:
                    try:
                        await ultroid_bot(
                            EditAdminRequest(
                                x.id,
                                user,
                                _gdemote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            elif "channel" in key.lower():
                if x.is_channel:
                    try:
                        await ultroid_bot(
                            EditAdminRequest(
                                x.id,
                                user,
                                _gdemote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            else:
                if x.is_group or x.is_channel:
                    try:
                        await ultroid_bot(
                            EditAdminRequest(
                                x.id,
                                user,
                                _gdemote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
        return await eor(ev, f"Demoted {name.first_name} in Total : {c} {key} chats.")


