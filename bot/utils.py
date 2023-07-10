import subprocess
import os
from google.cloud import speech
from telegram.ext import MessageHandler, Filters, Updater
from bot.constants import GOOGLE_APPLICATION_CREDENTIALS
import json
from jiwer import wer


def download_voice_file(file_id, context):
    voice_file = context.bot.getFile(file_id)
    ogg_file_path = 'voice.ogg'
    voice_file.download(ogg_file_path)
    return ogg_file_path


# Converts the downloaded OGG voice file to WAV format
def convert_to_wav(ogg_file_path):
    wav_file_path = 'voice.wav'
    subprocess.run(['ffmpeg', '-i', ogg_file_path,
                   '-ac', '1', '-y', wav_file_path])
    return wav_file_path


#  Converts the WAV file to mono format
def convert_to_mono(wav_file_path):
    mono_file_path = 'voice_mono.wav'
    subprocess.run(['ffmpeg', '-i', wav_file_path,
                   '-ac', '1', '-y', mono_file_path])
    return mono_file_path


#  Reads the content of an audio file
def read_audio_file(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        content = audio_file.read()
    return content


# Configures the speech recognition settings
def create_recognition_config():
    return speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=48000,
        language_code='en-US',
        enable_automatic_punctuation=True,
        model='default'
    )


# the speech recognition
def recognize_speech(config, audio):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS
    client = speech.SpeechClient()
    response = client.recognize(config=config, audio=audio)
    if response.results:
        return response.results[0].alternatives[0].transcript
    else:
        return "Sorry ,there is no  speech detected"


# -----------------------------------------------------------


def calculate_wer(transcription, reference):
    return wer(reference, transcription)


def update_jsonfile(jsonfile, transcription):
    with open(jsonfile, 'r') as file:
        data = json.load(file)# google-cloud-storage==2.1.0

    data['transcription'] = transcription
    original_text = data['original_text']
    data['wer'] = calculate_wer(transcription, original_text)

    with open(jsonfile, 'w') as file:
        json.dump(data, file)


def load_jsonfile(jsonfile):
    with open(jsonfile, 'r') as file:
        data = json.load(file)
    return data['original_text']


def voice_message(update, context):
    ogg_file_path = download_voice_file(update.message.voice.file_id, context)
    # ogg_file_path = download_voice_file(update.message.voice.file_id)
    wav_file_path = convert_to_wav(ogg_file_path)
    mono_file_path = convert_to_mono(wav_file_path)
    content = read_audio_file(mono_file_path)
    config = create_recognition_config()
    transcription = recognize_speech(
        config, speech.RecognitionAudio(content=content))

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Thank you for your voice message. Here is the text transcription:")
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=transcription)

    update_jsonfile(jsonfile, transcription)
    original_text = load_jsonfile(jsonfile)
    wer_result = calculate_wer(transcription, original_text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Word Error Rate (WER): {wer_result}")

    

voice_message_handler = MessageHandler(Filters.voice, voice_message)


