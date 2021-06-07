import telebot
from flask import Flask, request
import os

bot_token = '1813474286:AAFeptrH4_olk2uNP8eN9b5mK-bAb56CEF0'

bot = telebot.TeleBot(token=bot_token)
server = Flask(__name__)

def find_at(msg):
    for text in msg:
        if '@' in text:
            return text

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'welcome')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'to use this bot please give me your username')






@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://floating-cliffs-96478.herokuapp.com/ ' + 1813474286:AAFeptrH4_olk2uNP8eN9b5mK-bAb56CEF0)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    