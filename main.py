#6589678614:AAEKwUHM-Z52EdphhU5Pq9OA6f7z5agQA4Y
import telebot
from datetime import datetime
from pyrogram import*
from api import*
import time
from telebot import types

bot = telebot.TeleBot('6674817782:AAHhnyWV0hs3oLC9aOG40_HJzg3AhTJZKy4')

rusl = {'й': 1 ,'ц':2,'у':3,'к':4,'е':5,'н':6,'г':7,'ш':8,'щ':9,'з':10,'х':11,'ъ':12,'ф':13,'ы':14,'в':15,'а':16,'п':17,'р':18,'о':19,'л':20,'д':21,'ж':22,'э':23,'я':24,'ч':25,'с':26,'м':27,'и':28,'т':29,'ь':30,'б':31,'ю':32,'ё':33}



def Coding(strr):
    strr = strr.lower()
    code = ''
    for i in strr:
        if (rusl.get(i)) == None:
            code = code + " "
        else:
            code = code + str((rusl.get(i))) + " "

    return code
def deCoding(strr):

    if strr[len(strr) - 1] != " ":
        strr = strr + " "
    j = ''
    code = ''
    codl = []
    for i in strr:
        if i != " ":
            j = j + i

        if i == " ":
            for k in rusl.items():
                if str(k[1])==j:
                    code = code + (k[0])


            codl.append(j)
            j = ""


    return code
@bot.message_handler(commands=["start"])
def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Зашифровать')
    item2 = types.KeyboardButton('Расшифровать')

    markup.row(item1, item2)
    bot.send_message(message.chat.id,
                     'Здравствуйте,что вы хотите сделать?',
                     reply_markup=markup)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Зашифровать':
        sent = bot.send_message(message.from_user.id,'Введите текст')
        bot.register_next_step_handler(sent, stringg)
    if message.text == 'Расшифровать':
        sent = bot.send_message(message.from_user.id, 'Введите текст')
        bot.register_next_step_handler(sent, stringgg)
def stringg(message):
        trr = str(message.text)
        bot.send_message(message.chat.id, 'Закодированный текст:\n' + Coding(trr))


def stringgg(message):

    trr = str(message.text)
    bot.send_message(message.chat.id, 'Закодированный текст:\n' + deCoding(trr))




bot.polling()









