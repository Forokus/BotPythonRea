# -*- coding: utf-8 -*-
import Config
import telebot
import random
import Json


bot = telebot.TeleBot(Config.t_token)
spisok = Json.decode_json('Spisok_postov')

@bot.message_handler(regexp="/pynews")
def repeat_all_messages(message): 
	bot.send_message(message.chat.id, spisok.pop(random.randint(0, len(spisok)-1)))
	
@bot.message_handler(content_types=['text'])
def repeat_all_messages(message): 
	bot.send_message(message.chat.id, 'Привет!Напиши мне /pynews и я тебе пришлю пост из вк, посвященный языку программирования Python')

if __name__ == '__main__':
     bot.polling(none_stop=True)
