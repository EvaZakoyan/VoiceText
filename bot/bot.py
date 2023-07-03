from telegram.ext import Updater
from commands.start_button import *
from commands.help_button import *
from bot.utils import voice_message


# from utils import voice_message
from constants import BOT_TOKEN

def start_bot():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(start_button)
    dispatcher.add_handler(help_button)
    dispatcher.add_handler(voice_message)

    # updater.start_polling()
    # updater.idle()
