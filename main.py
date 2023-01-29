
from pymongo import MongoClient
import requests
import random
import os
import re
from re import IGNORECASE, escape, search
from telegram import Update
from telegram.error import TelegramError
from telegram.error import BadRequest
from telegram.constants import ParseMode
from telegram.ext import ContextTypes, CommandHandler, filters as Filters, MessageHandler, CallbackQueryHandler
import telegram.ext as tg
import re
from telegram.ext import Application
import asyncio
from typing import Union, List, Dict, Callable, Generator, Any
import itertools
from collections.abc import Iterable
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton

from telegram import Chat, ChatMember, Update, User
from functools import wraps


BOT_TOKEN = "6189386469:AAExpfLaZu4rZq9qnTv-ttcI4LLEPKAIKw0"


application = Application.builder().token(BOT_TOKEN).build()
asyncio.get_event_loop().run_until_complete(application.bot.initialize())
BOT_ID = application.bot.id



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    msg = update.effective_message
    await msg.reply_text(f"Hello, I Am Alive")

START = CommandHandler(["start", "ping"], start, block=False)

application.add_handler(START)

print("INFO: BOTTING YOUR CLIENT")
application.run_polling()
