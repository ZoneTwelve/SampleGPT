#!/usr/bin/env python3
# coding=utf-8
import logging
from dotenv import load_dotenv

from Command import *
from TelegramApi import app

from telegram.ext import CommandHandler, MessageHandler, filters

load_dotenv()
logging.basicConfig(level=logging.INFO)

# Main
def main():
    app.add_handler(CommandHandler('start', startbot))
    app.add_handler(MessageHandler(filters.Sticker, getSticker))

    # run
    logging.info("Bot Server Running...")
    app.run_polling(stop_signals=None)

if __name__ == '__main__':
    main()

