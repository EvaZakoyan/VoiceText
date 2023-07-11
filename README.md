# Voice-to-Text Telegram Bot

This is a Telegram bot that converts voice messages to text. The bot is capable of processing voice messages in English and Russian languages and provides functionality to calculate the Word Error Rate (WER) for the converted text.



## Installation

1. Clone the repository:
   
git clone https://github.com/your-username/telegram-voice-to-text-bot.git

2. Install the required dependencies:
   
pip install -r requirements.txt

3.Go to Google Cloud and set up a new project. You will need Google Speech API.  Set up the Google Cloud credentials by following the instructions provided by Google. 

4.Generate new service account and download a private key as JSON
  Set environment variable GOOGLE_APPLICATION_CREDENTIALS to the file path of the JSON key (see here for more instructions
  
5.Update the `GOOGLE_APPLICATION_CREDENTIALS` and `JSON_FILE_PATH` constants in the `bot/constants.py` file with the respective paths to your Google Cloud credentials and JSON file.



## Usage

1. Run the bot using the following command:

python main.py


2. Start a conversation with the bot on Telegram.

3. Send a voice message to the bot, and it will convert the message to text and calculate the WER.


## Requirements

To run this bot, you need to have the following dependencies installed:

- `google-cloud-speech==2.12.0`
- `python-telegram-bot==13.11`
- `psycopg2-binary==2.9.3`





