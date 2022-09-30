from argparse import Action
from gc import callbacks
import time
import telebot
import subprocess
import datetime
from datetime import datetime
import pytz
import json
import urllib
import traceback
import os
import sys
import aiogram
import asyncio
import threading

from telebot import util
from valuts import get_price

from TorSearch import TSearch
from Tsearch2 import get_torrents
from pycbrf import ExchangeRates

from telebot import TeleBot
from telebot import types
from time import sleep
from telethon import TelegramClient, events
import instaPy

#sys.path.insert(1, '/root/gdzstoler')
#import gdzstoler_v2

#Получаются на оф сайте телеграм// https://my.telegram.org/auth?to=apps
api_id=7427530
api_hash='86945cc35c57c8131c16566cb37f0249'



bot = telebot.TeleBot('1425712105:AAFYULRzpG0oiInjOsy8fz79DnDTRyC7uIs')  #Токен телеграм бота

## @getidsbot || bot for getting id


print('bot is active')



  

#Клавиатура 1
mm1 = types.ReplyKeyboardMarkup(row_width=1)
button2 = types.KeyboardButton("Книги")
button3 = types.KeyboardButton("Ссылки")
button4 = types.KeyboardButton("Курсы")
button5 = types.KeyboardButton("Тест")
button6 = types.KeyboardButton("Курсы крипты")
mm1.row(button2, button3)
mm1.row(button4, button5)
mm1.add(button6)


#Блок команд
@bot.message_handler(commands=['start'])  #---------------start----------
def start_command(message):
    kb_t = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton(text='Help', callback_data='0')
    kb_t.add(btn_1)
    bot.send_message(message.chat.id,
                     'Вы запустили бота активной воздушной поддержки-Athem\n' +
                     'Вас никто не заставлял\n' +
                     'Впрочем удачи, да прибудет она в твоём сердце\n' + '\n' +
                     'Для просмотра списка команд введите /com\n/tsearch - поисковик торрентов',
                     reply_markup=kb_t)


@bot.message_handler(commands=['help'])  #/help
def t4_command(message):
    kb_t4 = types.InlineKeyboardMarkup()
    url_btn_1 = types.InlineKeyboardButton(text='Клавиатура 1',
                                           callback_data='1')
    url_btn_2 = types.InlineKeyboardButton(text='Клавиатура 2',
                                           callback_data='2')
    url_btn_3 = types.InlineKeyboardButton(text='Локация ', callback_data='3')
    kb_t4.row(url_btn_1)
    #kb_t4.row(url_btn_2)
    kb_t4.row(url_btn_3)

    bot.send_message(message.chat.id, "Помощь\n/tsearch - поисковик торрентов\n"+
    "/you_get - загрузчик видео из тик тока\n"+
    "/inst_dn - загрузчик видео из инсты(тест)", reply_markup=kb_t4)


@bot.message_handler(commands=['courses'])  #/courses_1
def crs_command(message):
    kb_t5 = types.InlineKeyboardMarkup()
    urll_btn_0 = types.InlineKeyboardButton(text='Stuff for creatives',
                                            callback_data='7')
    urll_btn_1 = types.InlineKeyboardButton(text='TeraBox', callback_data='4')
    urll_btn_2 = types.InlineKeyboardButton(
        text='GDrive',
        url=
        'https://ancient-mountain-0f31.max-lils2013.workers.dev/'
    )
    urll_btn_3 = types.InlineKeyboardButton(
        text="OneDrive",
        url=
        'https://pb82-my.sharepoint.com/:f:/g/personal/jacksp1489_t_5tb_in/Et4QlVo-vm9PibYH96h8tVkBM2r9kIR4bgAucORwKbhrIw?e=Mtchzl'
    )
    kb_t5.row(urll_btn_0)
    kb_t5.row(urll_btn_1)
    kb_t5.row(urll_btn_2)
    kb_t5.row(urll_btn_3)

    bot.send_message(message.chat.id,
                     "Courses\nПока все в одной папке",
                     reply_markup=kb_t5)


@bot.message_handler(commands=['Links'])  #/Links
def link_keyboard(message):
    kb_t5 = types.InlineKeyboardMarkup()
    urll_btn_0 = types.InlineKeyboardButton(
        text="SOFT_GDRIVE",
        url=
        'https://drive.google.com/drive/folders/1o6dhZI1WeXE98jh3oLOXwALpG9aD4jbI?usp=sharing'
    )
    urll_btn_1 = types.InlineKeyboardButton(
        text="[HACKER]",
        url=
        'https://drive.google.com/drive/folders/12PPM4aDLBeMOrW61ubgzYyRyg3Y-W9h8?usp=sharing'
    )
    kb_t5.row(urll_btn_0,urll_btn_1)
    bot.send_message(message.chat.id,
                     "Courses\n Current links",
                     reply_markup=kb_t5)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == '0':
            t4_command(call.message)
        if call.data == '1':
            com_command(call.message)
        if call.data == '2':
            com_command2(call.message)
        if call.data == '3':
            location_command(call.message)
        if call.data == '4':
            crs_var_command(call.message, 'motion')
        if call.data == '5':
            Curlink_keyboard(call.message)
        if call.data == '6':
            stcp_command(call.message)
        if call.data == '7':
            crs_var_command(call.message, 'stuffcreative')
        


def crs_var_command(message, var):
    if var == 'motion':
        bot.send_message(
            message.chat.id,
            'Link:https://terabox.com/s/1pbiYUD-Wcjn12ZkPEvN90A\nPassword:px7d'
        )
    elif var == 'stuffcreative':
        bot.send_message(
            message.chat.id,
            'Link:https://terabox.com/s/1E8DKW2v1Plzslg3jytpQYA\nPassword:y28r'
        )


@bot.message_handler(commands=['com'])  #/com
def com_command(message):
    bot.send_message(message.chat.id, text='keyboard first', reply_markup=mm1)


@bot.message_handler(commands=['com2'])  #/com2
def com_command2(message):
    bot.send_message(message.chat.id, text='keyboard second', reply_markup=mm2)


#Клавиатура курсов валют
@bot.message_handler(commands=['exchange'])
def exchange_command(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    button_back = types.KeyboardButton(text="Вернуться к основной клавиатуре")
    itembtn1 = telebot.types.KeyboardButton('USD')
    itembtn2 = telebot.types.KeyboardButton('EUR')
    itembtn4 = telebot.types.KeyboardButton('Any crypto')
    markup.add(button_back)
    markup.row(itembtn1, itembtn2)
    markup.row(itembtn4)
    bot.send_message(chat_id=message.chat.id,
                     text='Курсы валют',
                     reply_markup=markup,
                     parse_mode="html")





@bot.message_handler(commands=["location"])
def location_command(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_back = types.KeyboardButton(text="Вернуться к основной клавиатуре")
    button_phone = types.KeyboardButton(text="Отправить номер телефона",
                                        request_contact=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение",
                                      request_location=True)
    keyboard.add(button_back, button_phone, button_geo)
    bot.send_message(message.chat.id,
                     "Поделиться инфой!!",
                     reply_markup=keyboard)

##input notes
@bot.message_handler(commands=["input"])
def input_final(message):
    global str
    input_command(message)


def input_command(message):
    send = bot.send_message(message.chat.id, "Введите название")
    bot.register_next_step_handler(send, input_com2)


def input_com2(message):
    global str
    str = message.text + '`'
    send = bot.send_message(message.chat.id, "Введите ссылку")
    bot.register_next_step_handler(send, input_com3)


def input_com3(message):
    global str
    str = str + message.text
    bot.send_message(message.chat.id, str.split('`')[0])
    bot.send_message(message.chat.id, str.split('`')[1])
    testexcel.input_note(str.split('`')[0], str.split('`')[1])


@bot.message_handler(commands=["check_notes"])
def check_notes(message):
    bot.send_message(message.chat.id,
                     text=testexcel.sheetpiece_out(1, 'max', "Notes.xlsx"))


#траблы с выводом, он как бы работает снизу вверх, не круто

curDay = datetime.now().day
@bot.message_handler(commands=[f'h{curDay}'])  #/stcp
def stcp_command(message):
    bot.send_message(message.chat.id,
                     text=testexcel.sheetpiece_out(5, 14, "Links.xlsx"))


@bot.message_handler(commands=['CurLinks'])  #/stcp
def Curlink_keyboard(message):
    bot.send_message(message.chat.id,
                     text=testexcel.sheetpiece_out(16, 20, "Links.xlsx"))



#GET CRYPTO
@bot.message_handler(commands=["crypto"])
def get_price1(message):
    send = bot.send_message(message.chat.id, "Write crypto symbol")
    bot.register_next_step_handler(send, get_price2)

def get_price2(message):
    bot.send_message(message.chat.id, get_price(message.text))



##GET TORRENTS 
@bot.message_handler(commands=['tsearch'])  #/com2
def com_command25(message):
    send = bot.send_message(message.chat.id, "Введите название")
    try:
      bot.register_next_step_handler(send, com_command26)
    except:
        bot.send_message(message.chat.id, " No result")


@bot.message_handler(commands=['tsearch2'])  #/com2
def com_command25_2(message):
    send = bot.send_message(message.chat.id, "Введите название")
    try:
      bot.register_next_step_handler(send, com_command27)
    except:
        bot.send_message(message.chat.id, " No result")      


def com_command26(message):
    TSearch(message.text)
    file = open("t4.txt", "rb")
    bot.send_document(message.chat.id, file)

def com_command27(message):
  get_torrents(message.text)
  file = open("_result.txt", "rb")
  bot.send_document(message.chat.id, file)


@bot.message_handler(commands=['you_get'])  #/you-get
def you_get_1(message):
  send = bot.send_message(message.chat.id, "Введите ссылку на видео(tiktok only)")
  try:
    bot.register_next_step_handler(send, you_get_2)
  except:
    bot.send_message(message.chat.id, " No result")

def you_get_2(message):
    print(message.text)
    
    try:
        if not 'playlist' in message.text:
            subprocess.call(['you-get',message.text,'-O','file'])
            file = open("file.mp4", "rb")
            bot.send_document(message.chat.id, file)
            subprocess.call(['rm','file.mp4'])
        elif 'playlist' in message.text:
            subprocess.call(['you-get',message.text,'-o','/root/tgbot/files/tmp'])
    except:
        bot.send_message(message.chat.id, "you-get noy found\nWAIT\n i will be install it")
        subprocess.call(['python3.10','-m','pip','install','you_get'])
        you_get_2(message)

#Instagram video downloader
@bot.message_handler(commands=['inst_dn'])  #/you-get
def instpy1(message):
  send = bot.send_message(message.chat.id, "Введите ссылку на видео: ")
  try:
    bot.register_next_step_handler(send, instpy2)
  except:
    bot.send_message(message.chat.id, " No result")

def instpy2(message):
  print(message.text)
  instaPy.get_content(message.text)
  file=open('files/video.mp4','rb')
  bot.send_document(message.chat.id,file)
  subprocess.call(['rm','files/video.mp4'])


#GDZSTOLER framework
@bot.message_handler(commands=["gdzstol"])
def gdz1(message):
    global link
    global num
    global path
    gdz2(message)


def gdz2(message):
    send = bot.send_message(message.chat.id, "Введите ссылку")
    bot.register_next_step_handler(send, gdz3)

def gdz3(message):
    global link
    link = message.text
    send = bot.send_message(message.chat.id, "Количество глав(1 если глава 1)")
    bot.register_next_step_handler(send, gdz4)

def gdz4(message):
    global num
    num =message.text
    send = bot.send_message(message.chat.id, "класс? ")
    bot.register_next_step_handler(send, gdz5)

def gdz5(message):
    global path
    path =message.text
    send = bot.send_message(message.chat.id, "предмет? ")
    bot.register_next_step_handler(send, gdz6)

def gdz6(message):
    global path
    path = path+'/'+message.text
    send = bot.send_message(message.chat.id, "название? ")
    bot.register_next_step_handler(send, gdz7)

def gdz7(message):
    global path
    global url
    global link
    path = path+'/'+message.text
    gdzstoler_v2.main(link,num,path)
    bot.send_message(message.chat.id,f'data:\nlink:{link}\nnum:{num}\npath:{path}' )
    


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    message_norm = message.text.strip().lower()

    if message.text == 'Привет':
        bot.send_message(message.chat.id, "Привет, чем я могу тебе помочь?")
    elif message.text == 'погода':
        bot.send_message(message.chat.id, 'https://www.gismeteo.ru/')
    elif message.text == 'курс':
        bot.send_message(message.chat.id,
                         'https://cbr.ru/currency_base/daily/')
    elif message.text == 'Читы':
        bot.send_message(message.chat.id, 'Аккаунты')
        file = open('Origin.txt', 'rb')
        bot.send_document(message.chat.id, file)
        file = open('steam.txt', 'rb')
        bot.send_document(message.chat.id, file)
    elif message.text == 'Книги':
        bot.send_message(
            message.chat.id,
            'Link:https://terabox.com/s/152AwSAd1jU7NxQDd6-hJrg\nPassword:4rqd'
        )

    elif message.text == 'Курсы':
        crs_command(message)
        
    elif message.text == 'Any crypto':
        get_price1(message)    

    elif message.text == 'Ссылки':
        link_keyboard(message)
    elif message.text == 'Курсы крипты':
        #os.system('python valuts.py')
        exchange_command(message)

    elif message_norm in ['usd', 'eur']:
        rates = ExchangeRates(datetime.now())
        bot.send_message(
            chat_id=message.chat.id,
            text=
            f"<b>{message_norm.upper()} курс сейчас: {float(rates[message_norm.upper()].rate)} RUB</b>",
            parse_mode="html")
    

    elif message.text == 'деанон':
        bot.send_message(
            message.chat.id,
            f'id: {message.chat.id}\nname: {message.from_user.first_name}' +
            f'\nlast name: {message.from_user.last_name}\nnick: {message.from_user.username}'
        )

    elif message.text == 'Вернуться к основной клавиатуре':
        com_command(message)
      
    

    



###Приём данных
### Прием фото
@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    try:
        chat_id = message.chat.id
 
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = f'files/' + file_info.file_path
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, f"Фото принято {message.caption}")
        
 
    except Exception as e:
        bot.reply_to(message, e)

### Прием документов
@bot.message_handler(content_types=['document'])
def handle_docs_doc(message):
    try:
        chat_id = message.chat.id
        
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        if message.caption==None:
                    src = 'files/documents/' + message.document.file_name
                    with open(src, 'wb') as new_file:
                        new_file.write(downloaded_file)
        elif message.caption!=None:
                os.mkdir(f'files/documents/{message.caption}')
                src = f'files/documents/{message.caption}/' + message.document.file_name
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)
        bot.reply_to(message, f"Документ принят {file_info.file_path}")
    except Exception as e:
        bot.reply_to(message, e)



### Прием аудио файлов
@bot.message_handler(content_types=['audio'])
def handle_docs_audio(message):
        try:
            chat_id = message.chat.id
        
            file_info = bot.get_file(message.audio.file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            if message.caption==None:
                src = 'files/music/' + message.audio.file_name
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)
                
            bot.reply_to(message, f"Трек принят {message.audio.file_name}")
        except Exception as e:
            bot.reply_to(message, e)
        ###Приём данных



#keep_alive()
bot.infinity_polling()




