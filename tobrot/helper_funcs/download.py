#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import io
import asyncio
import inspect
import os
import time
import sys
import traceback

from datetime import datetime
from pyrogram import Client, filters

from bs4 import BeautifulSoup
import urllib3

from tobrot import (
    MAX_MESSAGE_LENGTH,
    DOWNLOAD_LOCATION
)

from tobrot.helper_funcs.display_progress import progress_for_pyrogram

async def down_load_media_f(client, message):
    user_id = message.from_user.id
    print(user_id)
    mess_age = await message.reply_text("...", quote=True)
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    if message.reply_to_message is not None:
        start_t = datetime.now()
        download_location = "/app/"
        c_time = time.time()
        the_real_download_location = await client.download_media(
            message=message.reply_to_message,
            file_name=download_location,
            progress=progress_for_pyrogram,
            progress_args=(
                "trying to download", mess_age, c_time
            )
        )
        end_t = datetime.now()
        ms = (end_t - start_t).seconds
        LOGGER.info(the_real_download_location)
        await asyncio.sleep(6)
        await mess_age.edit_text(f"<b>OUTPUT:</b>\n\n <code>{the_real_download_location}</code> \n\n in <u>{ms}</u> seconds")
        the_real_download_location_g = os.path.basename(the_real_download_location)
        LOGGER.info(the_real_download_location_g)

    else:
        #await asyncio.sleep(4)
        await mess_age.edit_text("Reply to a Telegram Media, to save to the server.")


async def mass_down_load_media_f(client, message):
    user_id = message.from_user.id
    print(user_id)
    mess_age = await message.reply_text("...", quote=True)
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)    
    n=message.message_id
    w=message.reply_to_message.message_id
    tar_id = message.chat.id
    start_t = datetime.now()
    if message.reply_to_message is not None:
      for i in range(w, n):
          u_id = int(i)
          m = await client.get_messages(tar_id, u_id)
          if m.media:
              f = await m.download("/app/")
          end_t = datetime.now()
          ms = (end_t - start_t).seconds
          LOGGER.info(f)
          await asyncio.sleep(6)
          await mess_age.edit_text(f"<b>OUTPUT:</b>\n\n <code>{f}</code> \n\n in <u>{ms}</u> seconds")
          the_real_download_location_g = os.path.basename(f)
          LOGGER.info(the_real_download_location_g)
    else:
        #await asyncio.sleep(4)
        await mess_age.edit_text("Reply to a Telegram Media, to save to the server.")


async def scrap_seg_media_f(client, message):
    
    http = urllib3.PoolManager()

    url = message.reply_to_message.text
    n = message.text.split()
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, "html.parser")
    links = soup.find_all('a')

    for tag in links:
        link = tag.get('href',None)
        tght = tag.text.strip()
        if link and "ddrive" in link:
           if i < n:
              i = i+1
           else:
              await message.reply_text(f"<a href='{link}'>{tght}</a>")
