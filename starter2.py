import telebot
import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from google.cloud import speech
import subprocess
from pydub import AudioSegment

# # bot = telebot.TeleBot('6043277139:AAEmzcUPOpEGmtT2YOjKdDTaU-Ym-tOXiPQ')

# # @bot.message_handler(commands=['start'])
# # def main(message):
# #     bot.send_message(message.chat.id, f'Hello,{message.from_user.first_name}')

# # @bot.message_handler(commands=['info'])
# # def main(message):
# #     bot.send_message(message.chat.id, 'This is a simple Telegram bot that converts voice messages to text using Google '
# #                                       'Speech. Can be found at @voicemessage_to_text_bot, crated by Y.Zakoyan')

# # bot.infinity_polling()



# # Version 1 , not using decoraters , using Updater , Filters , etc 

# BOT_TOKEN = '6043277139:AAEmzcUPOpEGmtT2YOjKdDTaU-Ym-tOXiPQ'


# updater = Updater(token=BOT_TOKEN, use_context=True)
# dispatcher = updater.dispatcher

# # start block 
# def start_button(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Send me your voice message ")

# start_button_handler = CommandHandler('start', start_button)
# dispatcher.add_handler(start_button_handler)




# # help block 
# def help_button(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="This is a simple Telegram bot that converts voice messages to text using Google Speech. Can be found at @voicemessage_to_text_bot, crated by Y.Zakoyan")

# help_button_handler = CommandHandler('help', help_button)
# dispatcher.add_handler(help_button_handler)







# # Adding credintals of Google Speech ,adding the path to json key .
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/eva/Desktop/Telegram_bot/voice-message-to-text-bot-b8fd2b2691fe.json'



# def voice_message(update, context):
# # Getting the file 
#     voice_file = context.bot.getFile(update.message.voice.file_id)
    

#     ogg_file_path = 'voice.ogg'
#     voice_file.download(ogg_file_path)
# # Need to change to mono , for that need configure the ffmpeg ?? how 
# # The Speech-to-Text API requires audio input to be in mono format, which means it should have a single channel. Stereo audio contains two channels, left and right, whereas mono audio contains a single channel with combined audio information.
#     wav_file_path = 'voice.wav'
#     subprocess.run(['ffmpeg', '-i', ogg_file_path, '-ac', '1', wav_file_path]) 


#     client = speech.SpeechClient()



#     with open(wav_file_path, 'rb') as audio_file:
#         content = audio_file.read()

# # Need to set the sample_rate_hertz 48000 , Valid values are: 8000-48000.16000 is optimal.
#     audio = speech.RecognitionAudio(content=content)
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=48000,
#         language_code='en-US',
#         enable_automatic_punctuation=True,
#         model='default'
#     )


#     response = client.recognize(config=config, audio=audio)


#     transcription = response.results[0].alternatives[0].transcript


#     context.bot.send_message(chat_id=update.effective_chat.id, text=transcription)

# voice_handler = MessageHandler(Filters.voice, voice_message)
# dispatcher.add_handler(voice_handler)


# updater.start_polling()
# updater.idle()




# Create an Updater object and set up your bot token
# updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)
# dispatcher = updater.dispatcher

# def download_voice_file(file_id, file_path):
#     # voice_file = context.bot.getFile(file_id)
#     voice_file.download(file_path)

# def convert_to_mono(input_file, output_file):
#     subprocess.run(['ffmpeg', '-i', input_file, '-ac', '1', output_file])

def recognize_speech(file_path):
    client = speech.SpeechClient()

    with open(file_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=48000,
        language_code='en-US',
        enable_automatic_punctuation=True,
        model='default'
    )

    response = client.recognize(config=config, audio=audio)
    return response.results[0].alternatives[0].transcript

# def voice_message(update, context):
#     # Check if the message is a voice message
#     if update.message.voice:
#         # Download the voice file ogg ??
#         ogg_file_path = 'voice.ogg'
#         download_voice_file(update.message.voice.file_id, ogg_file_path)


#         # wav_file_path = 'voice.wav'
#         # convert_to_mono(ogg_file_path, wav_file_path)

#         # Perform speech recognition
#         transcription = recognize_speech(wav_file_path)

#         # Send the text message back to the user
#         context.bot.send_message(chat_id=update.effective_chat.id, text=transcription)
#     else:
#         raise TypeError("Only voice messages are allowed. Please try again.")








voice_handler = MessageHandler(Filters.voice, voice_message)
dispatcher.add_handler(voice_handler)


updater.start_polling()
updater.idle()
