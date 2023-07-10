from telegram.ext import Updater
from commands.start_button import *
from commands.help_button import *
from bot.utils import voice_message_handler
from bot.constants import BOT_TOKEN



def start_bot():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(start_button_handler)
    dispatcher.add_handler(help_button_handler)
    dispatcher.add_handler(voice_message_handler)
    
    return updater


