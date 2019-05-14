# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot('550209648:AAHwPCNrDYIiN-8IsJPSCtSGTxMzg7Svs5c')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()