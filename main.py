from bot.bot import start_bot



if __name__ == "__main__":
    updater = start_bot()
    updater.start_polling()
    updater.idle()