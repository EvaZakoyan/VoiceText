# help block
# from telegram.ext import Updater, CommandHandler 
# import constants


# updater = Updater(token=constants.BOT_TOKEN, use_context=True)
# dispatcher = updater.dispatcher


 
# def help_button(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="This is a simple Telegram bot that converts voice messages to text using Google Speech. Can be found at @voicemessage_to_text_bot, crated by Y.Zakoyan")

# help_button_handler = CommandHandler('help', help_button)
# dispatcher.add_handler(help_button_handler)


from telegram.ext import CommandHandler

def help_button(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="This is a simple Telegram bot that converts voice messages to text using Google Speech. Can be found at @voicemessage_to_text_bot, created by Y.Zakoyan")

help_button_handler = CommandHandler('help', help_button)
