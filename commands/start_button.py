# start block


from telegram.ext import CommandHandler

def start_button(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Send me your voice message ")

start_button_handler = CommandHandler('start', start_button)
