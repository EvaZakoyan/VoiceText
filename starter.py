import telebot
import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from google.cloud import speech
import subprocess
import constants

# Version 1 , not using decoraters , using Updater , Filters , etc

# BOT_TOKEN = '6043277139:AAEmzcUPOpEGmtT2YOjKdDTaU-Ym-tOXiPQ'


updater = Updater(token=constants.BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# start block
# def start_button(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Send me your voice message ")

# start_button_handler = CommandHandler('start', start_button)
# dispatcher.add_handler(start_button_handler)


# help block
# def help_button(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="This is a simple Telegram bot that converts voice messages to text using Google Speech. Can be found at @voicemessage_to_text_bot, crated by Y.Zakoyan")

# help_button_handler = CommandHandler('help', help_button)
# dispatcher.add_handler(help_button_handler)


# Adding credintals of Google Speech ,adding the path to json key .
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/eva/Desktop/Telegram_bot/voice-message-to-text-bot-d92d67095753.json'


def voice_message(update, context):
    # Getting the file
    voice_file = context.bot.getFile(update.message.voice.file_id)

    ogg_file_path = 'voice.ogg'
    voice_file.download(ogg_file_path)
# Need to change to mono , for that need configure the ffmpeg ?? how
# The Speech-to-Text API requires audio input to be in mono format, which means it should have a single channel. Stereo audio contains two channels, left and right, whereas mono audio contains a single channel with combined audio information.
    wav_file_path = 'voice.wav'


# Modified the subprocess ,deleted  input argument set to yes , set  the -y flag of ffmpeg automatically overwriting.
    subprocess.run(['ffmpeg', '-i', ogg_file_path,
                   '-ac', '1', '-y', wav_file_path])

    client = speech.SpeechClient()

    with open(wav_file_path, 'rb') as audio_file:
        content = audio_file.read()

# Need to set the sample_rate_hertz 48000 , Valid values are: 8000-48000.16000 is optimal.
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=48000,
        language_code='en-US',
        enable_automatic_punctuation=True,
        model='default'
    )

    response = client.recognize(config=config, audio=audio)

    transcription = response.results[0].alternatives[0].transcript

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Thank you for your voice message. Here is the text transcription:")
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=transcription)


voice_handler = MessageHandler(Filters.voice, voice_message)
dispatcher.add_handler(voice_handler)


updater.start_polling()
updater.idle()
