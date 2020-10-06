#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) PublicLeech Author(s)

import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import os
import time
from pyrogram.types import (
    Message
)
from tobrot import (
    DOWNLOAD_LOCATION
)

from tobrot.helper_funcs.extract_link_from_message import extract_link
from tobrot.helper_funcs.youtube_dl_extractor import extract_youtube_dl_formats

async def ytdl_btn_k(message: Message):
    i_m_sefg = await message.edit_text("processing")
    # LOGGER.info(message)
    # extract link from message
    dl_url, cf_name, yt_dl_user_name, yt_dl_pass_word = await extract_link(
        message.reply_to_message, "YTDL"
    )
    LOGGER.info(dl_url)
    LOGGER.info(cf_name)
    if dl_url is not None:
        current_user_id = message.reply_to_message.from_user.id
        # create an unique directory
        user_working_dir = os.path.join(
            DOWNLOAD_LOCATION,
            str(current_user_id),
            str(message.message_id)
        )
        # create download directory, if not exist
        if not os.path.isdir(user_working_dir):
            os.makedirs(user_working_dir)
        await i_m_sefg.edit_text("extracting links")
        # list the formats, and display in button markup formats
        thumb_image, text_message, reply_markup = await extract_youtube_dl_formats(
            dl_url,
            # cf_name,
            yt_dl_user_name,
            yt_dl_pass_word,
            user_working_dir
        )
        await i_m_sefg.edit_text(
            text=text_message,
            reply_markup=reply_markup
        )
    else:
        await i_m_sefg.delete()
