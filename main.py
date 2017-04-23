import logging
import telebot
from telebot.types import Message

from settings import BOT_TOKEN, SYNONYMS

bot = telebot.TeleBot(token=BOT_TOKEN)


@bot.message_handler(func=lambda msg: msg.chat.type == "group" or msg.chat.type == "supergroup")
def reply(message):
    text = message.text.lower()
    for marco in SYNONYMS:
        if marco in text:
            logging.info("Reply to " + message)
            bot.send_sticker(message.chat.id, open("sticker.webp", "rb"), message.message_id)
            break


bot.polling()
