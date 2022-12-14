import os
import telebot
from telegram.ext import Updater, CommandHandler
import requests
import json
import csv

# TODO: 1.1 Get your environment variables 
API_KEY =  "b1329187"
bot_token  = os.getenv('bot_token')
url = "http://www.omdbapi.com/"


bot = telebot.TeleBot('5781498130:AAE_VHLRpBISQIFQR5UULgVkVnC-ZOHaFFM')

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    global botRunning
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')

@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    global botRuuning
    bot.reply_to(message, 'Getting movie info...')
    movie_name = update.message.text.split()[1]
    movie_url = f"{url}?apikey={api_key}&t={movie_name}"
    response = requests.get(movie_url)
    with open("movie_data.json", "w") as f:
      json.dump(response.json(), f)
    update.message.reply_text(response.json())
    bot_token = "5781498130:AAE_VHLRpBISQIFQR5UULgVkVnC-ZOHaFFM"
    updater = Updater(bot_token, use_context=True)
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    global botRunning
    bot.reply_to(message, 'Generating file...')
    files = {"document" :open('movieinfo.csv','rb')} 
    resp = requests.post('https://api.telegram.org/bot5781498130:AAE_VHLRpBISQIFQR5UULgVkVnC-ZOHaFFM/sendDocument?chat_id=947054111', files=files)
    bot.reply_to(message, resp)
   
  
@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()
