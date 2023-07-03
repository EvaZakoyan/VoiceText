# start block
from telegram.ext import Updater, CommandHandler 
import constants
from bot import *

updater = Updater(token=constants.BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

 
def start_button(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Send me your voice message ")

start_button_handler = CommandHandler('start', start_button)
dispatcher.add_handler(start_button_handler)


