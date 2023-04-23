# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.
"""
✘ **Bantuan Untuk To Anime**

๏ **Perintah:** `toanime` <balas foto>
◉ **Keterangan:** Ubah gambar menjadi anime.

◉ **Note:** Wajah harus terdeteksi.
"""


import asyncio
import time

from telethon.tl.functions.contacts import (
    BlockRequest,
    GetBlockedRequest,
    UnblockRequest,
)
from . import *

@ayra_cmd(pattern="toanime")
async def convert_image(event):
    if not event.reply_to_msg_id:
        return await event.eor("**Mohon Balas Ke Foto**")
    bot = "@qq_neural_anime_bot"
    if event.reply_to_msg_id:
        cot = await event.respond("**Processing...**")
        await event.client(UnblockRequest(bot))
        ba = await event.client.forward_to(bot, event.reply_to_msg_id, event.chat_id)
        await asyncio.sleep(30)
        await ba.delete()
        await cot.delete()
        get_photo = []
        async for Toanime in client.iter_messages(bot, filter=InputMessagesFilterPhotos):
            get_photo.append(InputMediaPhoto(Toanime.photo))
        await event.client.send_file(
            event.chat_id,
            get_photo,
            reply_to=event.message.id,
        )