#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (C) PR0FESSOR-99

import os
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

USERNAME=Config.BOT_USERNAME


# start_Msg, help_msg, about_msg
# Team Mo Tect
MT = "@AutoCaptionAdder_Bot"


@Client.on_message(filters.private & filters.command("start"))
async def start_meg(client, update):
    text = f"""<b>Hello  👋 {update.from_user.mention}\n\nI am an AutoCaptionAdder bot,\n\nAdd me to your channel as admin, and I will show you my true purpose.\n\n {MT}</b>"""
    reply_markup =  InlineKeyboardMarkup( [[
        InlineKeyboardButton("FORK BY", url="t.me/theflaxcompany")
        ]]
    )
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
  )
