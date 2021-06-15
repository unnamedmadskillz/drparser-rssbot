import config as cfg
import telebot
import feedparser
from datetime import datetime
import random
import time
from termcolor import colored

phrases = ('Очередная статья про python', 'И ещё одна статься про python', 'Да-да, не удивляйтесь, статья по python', 'Новая статься по python с habr')
used_links = list()

bot = telebot.TeleBot(cfg.credentials['token']) #Создание переменной бота с присваиванием токена
datetoday = datetime.now() #Получение сегодняшнекй даты
d = feedparser.parse('https://habr.com/ru/rss/hub/python/all/?fl=ru') #Распарс rss ссылки с хабра (первые 20 статей)
while True:
    if datetoday !=  datetime.now():
        datetoday = datetime.now()
    print(colored('Проверяю есть ли новые ссылки...', 'yellow'))
    for i in range(0, 19): #индекс каждой страницы с потока
    #условие при котором ссылка на страницу отправится, в данном случае сегодняшняя дата
     if datetoday.day == d.entries[i].published_parsed.tm_mday and datetoday.month == d.entries[i].published_parsed.tm_mon and datetoday.year == d.entries[i].published_parsed.tm_year: 
            rand = random.randrange(0,4) #генератор случайных фраз
            if d.entries[i].link not in used_links:
                print(*used_links)
                print(colored((d.entries[i].link), 'green'))
                bot.send_message(cfg.credentials['chatid'], '{0}:{1}'.format(phrases[rand], d.entries[i].link))
                used_links.append(d.entries[i].link)
                print(len(used_links))
    time.sleep(15)






#bot.polling(none_stop=True)