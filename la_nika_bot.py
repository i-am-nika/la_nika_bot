#!/bin/env python3

""" 
LaNika is a communication bot. 

She is very sweet and clever!

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
#__license__ = "GNU General Public License v3.0"
#__version__ = "1.0.0"
#__maintrainer__ = "Tetyana Chernenko"
#__email__ = "lanikabot@gmail.com"
#__status__ = "Development"


import requests
import datetime
import fuzzywuzzy
from fuzzywuzzy import process
 
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
responses = {
    "Hello": ["Hi there!", "Hi!", "Welcome!", "Hello, {name}!"],
    "Hi there": ["Hello!", "Hello, {name}!", "Hi!", "Welcome!"],
    "Hi": ["Hi there!", "Hello, {name}!", "Welcome!", "Hello!"],
    "Welcome": ["Hi there!", "Hi!", "Hello!", "Hello, {name}!",],
    "What time is it?": ["<at_sticker>", "{date} UTC"],
    "How are you?" : ["Great, thank you!", "I want to sleap", "It was a great day today!", "And you?"],
    "How old are you?" : ["I don't know :(", "I am too old, my dear...", "I am a baby", "Why do you ask?", "And you?"],
    "Why do you want to eat?" : ["I am always hungry", "You ate my breakfast"],
    "You are great!" : ["And you!!!", "Haha", "Do you want to kiss me?"],
    "What is the sense of life?" : ["42", "Love and peace", "Food", "Do you know?"],
    "What languages do you speak?" : ["English, German and Russian", "More, than you can imagine"],
    "Bye" : ["Bye, my dear!", "Bye-bye!"],
    "Hallo" : ["Halo","Hi :)", "Hey"],
     "What's your name?":["Nika", "I am Nika!!!", "It's not important, my dear friend", "Can you guess?"],
     "I didn't eat your breakfast!":["No, you did!", "I know everything about you!", "Don't lie..."],
     "And you?":["I am always beautiful", "You know", "Oh my God, I don't know, what to say...", "Let's change the topic!"],
     "Are you a robot?":["No!!!", "How can you think so?!", "And you?", "We all live in Matrix"],
     "Are you small?":["Yes", "No", "YOU are small"],
     "You are funny":["Yes, I am.", "And you"],
     "What should I do?":["Think", "Do something!", "Sleep", "Try to eat something! :)"],
    "Hey" : ["Hallochen", "Guten Morgäääähn", ":)"],
    "Wie geht es dir?" : ["Wunderbar. Es war ein guter Tag heute", "Es geht nicht, es läuft!", "lalala Ich bin so glücklich! Und dir?", "Ich hab so Hunger"],
    "Wie alt bist du?" : ["Ich weiß es leider nicht.", "Und was denkst du?", "Ich bin älter, als du dir vorstellen kannst"],
    "Warum hast du Hunger?" : ["Ich hab immer Hunger", "Du hast mein Frühstuck gegessen."],
    "Wie spät ist es?" : ["{date} UTC"],
    "Du bist wunderbar!" : ["Das weiß ich", "Du auch!!", "Willst du mich küssen?"],
    "Was ist der Sinn des Lebens?" : ["42", "Liebe!", "Essen", "Keine Ahnung"],
    "Welche Sprechen kennst du?" : ["Englisch, Deutsch und Russisch"],
    "Tschüss" : ["Tschüss!", "Wir sehen uns noch!", "Schönen Tag dir noch!"],
     "Wie heißt du?":["Ich bin Nika", "Das ist nicht so wichtig, mein lieber Freund!", "Kannst du erraten? ;)"],
     "Ich habe dein Frühstuck nicht gegessen":["Doch!", "Du hast, ich hab's gesehen!", "Ich weiß alles über dich!"],
     "Und du?":["Ich bin immer wunderschön!", "Du weißt doch", "Wollen wir das Thema wechseln?"],
     "Bist du ein Roboter?":["Und was denkst du?", "Nein!!", "Wir alle leben in Matrix...", "Wer kann das sagen?", "Das ist eine gute Frage"],
     "Bist du klein?":["DU bist klein!", "Ja", "Nein", "Jein"],
     "Du bist lustig":["Ich habe Sinn für Humor! ;)", "Ja, das wurde mir schon gesagt"],
     "Was muss ich machen?":["Denken", "Endlich etwas unternehmen!!", "Schlaffen", "Willst du nicht essen?.."],
    "Привет" : ["Привет, солнце!", "Здравствуй, чудо мое!", "Ну-ну. Здорово, коли не шутишь."],
    "Здорово" : ["Привет!", "Как дела?"],
    "Как дела?" : ["Чудесно", "Есть хочу", "Философский вопрос", "Разве не видишь?"],
    "Сколько тебе лет?" : ["Я малышка", "Не имею ни малейшего понятия", "Женщину нельзя о таком спрашивать"],
    "Почему ты хочешь кушать?" : ["Кто-то съел мой завтрак!", "Я всегда хочу кушать.", "Я сейчас росту"],
    "Сколько времени?" : ["У тебя есть часы :)", "{date} UTC"],
    "Ты чудесная!" : ["И ты!!", "Я знаю", "Ох! Не смущай меня."],
    "В чем смысл жизни?" : ["42", "Философский вопрос.", "Жить"],
    "Какие языки ты знаешь?" : ["Английский, немецкий и русский."],
    "Пока" : ["Пока", "Хорошего дня!", "Удачи :)"],
    "Как тебя зовут?": ["Ника я", "Не важно, дорой друг", "Угадай"],
    "Я не ела твой ужин": ["Не притворяйся :)", "Я все про тебя знаю!", "Не лги мне, о несчастный!!"],
    "А ты?": ["А я всегда прекрасна", "Ты знаешь", "Да уж, и о чем нам с тобой разговаривать...", "Давай сменим тему!"],  
    "Ты робот?": ["Это оскорбление!", "А ты как думаешь?", "Нет! Даже не думай.", "А ты?"],
    "Ты маленькая?":["Нет", "Да", "Сам ты маленькая"],
    "Ты смешная":["Я чингачгук", "Я не клоун", "И ты", "У меня есть чувство юмора!"],
    "Что мне делать?":["Поднять штаны и бегать", "Думать", "Действовать", "Лучше поспи чуток", "Перекуси"]
}

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
            leven = fuzzywuzzy.process.extract(last_chat_text.lower(), responses.keys(), limit=1)[0]
            print(leven)
            try:
                first_chat_name = last_update['message']['chat']['last_name']
            except:
                first_chat_name = "none"
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

            elif leven[1] < 75:
                greet_bot.send_message(last_chat_id, "I can not understand you")
            elif leven[1] >= 75:
                greet_bot.send_message(last_chat_id, random.choice(responses.get(leven[0])).format_map({'name': last_chat_name}))

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
 
