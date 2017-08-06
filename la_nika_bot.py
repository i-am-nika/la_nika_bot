#!/bin/env python3

""" 
LaNika is a communication bot. 

She is just a small baby now and can only greet you in three languages. But she is very cute, intelligent and no doubt she'll learn many interestig thing very soon!

FIND NIKA:

    Look for @LaNikaBot in Telgram
    Greet her in English, German or Russian
    Follow Nika on twiter (www.twitter.com/LaNikaBot) to get updates
"""

#la_nika_bot.py
#usage:
#$ ./la_nika_bot.py
 #__author__ = "Tetyana Chernenko"
#__copyright__ = "Copyright (c) 2017 Tetyana Chernenko"
#__credits__ = ["Tetyana Chernenko"]
#__license__ = "Public Domain"
#__version__ = "1.0.0"
#__maintrainer__ = "Tetyana Chernenko"
#__email__ = "lanikabot@gmail.com"
#__status__ = "Development"


import requests
import datetime
 
token = <your token>

class BotHandler:
 
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
 
    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json
 
    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp
 
    def get_last_update(self):
        get_result = self.get_updates()
 
        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result
            
        return last_update

greet_bot = BotHandler(token)  
greetings = ('здравствуй', 'привет', 'ку', 'здорово', "приветище", "добрый день", "доброе утро", "добрый вечер", "доброй ночи", 'здравствуй, ника', 'привет ника', 'куку, ника', 'здорово, ника', "приветище, ника", "добрый день, ника", "доброе утро, ника", "добрый вечер, ника", "доброй ночи, ника", "привет!")  
greetings_eng = ("hi", "hello", "hey", "good morning", "good evening", "good day", "hi nika", "hello nika", "hey nika", "good morning nika", "good evening nika", "good day nika", "hi!", "hello!", "hi nika!")
greetings_de = ("hallo", "guten morgen", "guten tag", "guten abend", "nika", "hallo nika", "guten morgen nika", "guten tag nika", "guten abend nika", "hallo!", "hey!", "hallo nika!")
now = datetime.datetime.now()

def write_chats(filename, information, today):
    new = open(filename, "a")
    new.write(today+"\n")
    new.write(str(information) + "\n") 
 
def main():  
    new_offset = None
    hour = now.hour
 
    while True:
        greet_bot.get_updates(new_offset)
 
        last_update = greet_bot.get_last_update()
        print("LAST UPDATE: ", type(last_update), "\n", last_update)

        if type(last_update) != list:
            last_update_id = last_update['update_id']
            last_chat_text = last_update['message']['text']
            print(last_chat_text, len(last_chat_text), type(last_chat_text))
            last_chat_id = last_update['message']['chat']['id']
            last_chat_name = last_update['message']['chat']['first_name']
            first_chat_name = last_update['message']['chat']['last_name']

            if last_chat_text.lower() in greetings and 6 <= hour < 12:
                greet_bot.send_message(last_chat_id, 'Доброе утро, {}! :-)'.format(last_chat_name))
                greet_bot.send_message(last_chat_id, 'Я так кушать хочу... ')

            elif last_chat_text.lower() in greetings_eng and 6 <= hour < 12:
                greet_bot.send_message(last_chat_id, 'Good morning, {}! :-)'.format(last_chat_name))
                greet_bot.send_message(last_chat_id, 'I want to eat so much... ')

            elif last_chat_text.lower() in greetings_de and 6 <= hour < 12:
                greet_bot.send_message(last_chat_id, 'Guten Morgen, {}! :-)'.format(last_chat_name))
                greet_bot.send_message(last_chat_id, 'Ich hab so Hunger... ')

            elif last_chat_text.lower() in greetings and 12 <= hour < 17:
                greet_bot.send_message(last_chat_id, 'Добрый день, {}! :-)'.format(last_chat_name))
                greet_bot.send_message(last_chat_id, 'Я так кушать хочу... ')

            elif last_chat_text.lower() in greetings_eng and 12 <= hour < 17:
                greet_bot.send_message(last_chat_id, 'Good day, {}! :-)'.format(last_chat_name))
                greet_bot.send_message(last_chat_id, 'I want to eat so much... ')

            elif last_chat_text.lower() in greetings_de and 12 <= hour < 17:
                greet_bot.send_message(last_chat_id, 'Guten Tag, {}! :-)'.format(last_chat_name))
                greet_bot.send_message(last_chat_id, 'Ich hab so Hunger... ')

            elif last_chat_text.lower() in greetings and 17 <= hour <= 23:
                greet_bot.send_message(last_chat_id, 'Добрый вечер, {}! :-)'.format(last_chat_name))
                greet_bot.send_message(last_chat_id, 'Я так кушать хочу... ')

            elif last_chat_text.lower() in greetings_eng and 17 <= hour <= 23:
                greet_bot.send_message(last_chat_id, 'Good evening, {}!  :-)'.format(last_chat_name))
                greet_bot.send_message(last_chat_id, 'I want to eat so much... ')

            elif last_chat_text.lower() in greetings_de and 17 <= hour <= 23:
                greet_bot.send_message(last_chat_id, 'Guten Abend, {}! :-)'.format(last_chat_name))
                greet_bot.send_message(last_chat_id, 'Ich hab so Hunger... ')
            
            else:
                greet_bot.send_message(last_chat_id, 'I don\'t understand, {}. I\'m just a small baby! :-) \nЯ не понимаю, {}, я еще малышка! :-) \nI verstehe nicht, {}, ich bin noch ein Baby! :-)'.format(last_chat_name, last_chat_name, last_chat_name))

            write_chats(last_chat_name+"_"+first_chat_name, last_update, str(datetime.datetime.now())) 
            new_offset = last_update_id + 1

        else:
             print("No updates")

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()
 
