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
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import os

from tobrot import (
    DOWNLOAD_LOCATION,
    TG_BOT_TOKEN,
    APP_ID,
    API_HASH,
    AUTH_CHANNEL,
    EXEC_CMD_TRIGGER,
    Ytdl_CMD_TRIGGER,
    Eval_CMD_TRIGGER,
    Upload_CMD_TRIGGER,
    Save_Thumb_CMD_TRIGGER,
    Clear_thumb_CMD_TRIGGER,
    TELEGRAM_CMD_TRIGGER,
    Mass_CMD_TRIGGER,
    Scrapx_CMD_TRIGGER,
    Mux_CMD_TRIGGER,
    Muxdo_CMD_TRIGGER
)

from pyrogram import (
    Client,
    filters
)
from pyrogram.handlers import (
    MessageHandler,
    CallbackQueryHandler
)

from tobrot.plugins.myown import mux_f, mux_do_f
from tobrot.plugins.new_join_fn import new_join_f, help_message_f
from tobrot.plugins.incoming_message_fn import incoming_youtube_dl_f
from tobrot.plugins.status_message_fn import (
    exec_message_f,
    eval_message_f,
    upload_document_f
)
from tobrot.plugins.call_back_button_handler import button
from tobrot.plugins.custom_thumbnail import (
    save_thumb_nail,
    clear_thumb_nail
)

from tobrot.helper_funcs.download import down_load_media_f, mass_down_load_media_f , scrap_seg_media_f

if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    #
    app = Client(
        ":memory:",
        bot_token=TG_BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        workers=343,
        workdir=DOWNLOAD_LOCATION
    )
    #
    incoming_youtube_dl_handler = MessageHandler(
        incoming_youtube_dl_f,
        filters=filters.command([Ytdl_CMD_TRIGGER]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(incoming_youtube_dl_handler)
    #
    incoming_mass_download_handler = MessageHandler(
        mass_down_load_media_f,
        filters=filters.command([Mass_CMD_TRIGGER]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(incoming_mass_download_handler)
    #
    incoming_scrap_handler = MessageHandler(
        scrap_seg_media_f,
        filters=filters.command([Scrapx_CMD_TRIGGER]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(incoming_scrap_handler)
    #
    incoming_telegram_download_handler = MessageHandler(
        down_load_media_f,
        filters=filters.command([TELEGRAM_CMD_TRIGGER]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(incoming_telegram_download_handler)
    #
    incoming_mux_handler = MessageHandler(
        mux_f,
        filters=filters.command([Mux_CMD_TRIGGER]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(incoming_mux_handler)
    #
    incoming_mux_do_handler = MessageHandler(
        mux_do_f,
        filters=filters.command([Muxdo_CMD_TRIGGER]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(incoming_mux_do_handler)
    #
    exec_message_handler = MessageHandler(
        exec_message_f,
        filters=filters.command([EXEC_CMD_TRIGGER]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(exec_message_handler)
    #
    eval_message_handler = MessageHandler(
        eval_message_f,
        filters=filters.command([Eval_CMD_TRIGGER]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(eval_message_handler)
    #
    upload_document_handler = MessageHandler(
        upload_document_f,
        filters=filters.command([Upload_CMD_TRIGGER]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(upload_document_handler)

    help_text_handler = MessageHandler(
        help_message_f,
        filters=filters.command(["help"]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(help_text_handler)
    #
    new_join_handler = MessageHandler(
        new_join_f,
        filters=~filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(new_join_handler)
    #
    call_back_button_handler = CallbackQueryHandler(
        button
    )
    app.add_handler(call_back_button_handler)
    #
    save_thumb_nail_handler = MessageHandler(
        save_thumb_nail,
        filters=filters.command([Save_Thumb_CMD_TRIGGER]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(save_thumb_nail_handler)
    #
    clear_thumb_nail_handler = MessageHandler(
        clear_thumb_nail,
        filters=filters.command([Clear_thumb_CMD_TRIGGER]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(clear_thumb_nail_handler)
    #
    app.run()
