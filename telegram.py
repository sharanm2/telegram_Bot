import os
import telebot  # Use 'telebot' to import the library

API_KEY = os.getenv('API_KEY')
print(API_KEY)
bot = telebot.TeleBot(API_KEY)  # Use 'telebot.TeleBot' for the class name
print("Starting")
@bot.message_handler(commands=['Greet'])  # Use 'commands' instead of 'command'
def greeting(message):
    bot.send_message(message.chat.id, "Hello")

bot.polling()

