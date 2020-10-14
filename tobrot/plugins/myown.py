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


import os

from tobrot import (
    DOWNLOAD_LOCATION
)

import asyncio
import time
from tobrot.helper_funcs.help_Nekmo_ffmpeg import mux_video , mux_do_video

async def mux(client, message):
    status_message = await message.reply_text("Processing ...")
    a , b , c= message.text.split("|", 1)
    location = await mux_video(a,b,c)
    await status_message.edit(location)
    
async def mux_do(client, message):
    status_message = await message.reply_text("Processing ...")
    a , b = message.text.split("|", 1)
    location = await mux_do_video(a,b)
    await status_message.edit(location)
