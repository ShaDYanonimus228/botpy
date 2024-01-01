import telebot
from telebot import types
import requests
import openai
bot = telebot.TeleBot('6916784411:AAEomkZPFmGMnKRKB2Kdt5IuyeCD4aLBBVc')

def chatgpt(question):
    openai.api_key = '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'

    user_question = question

    # Отправьте запрос к GPT-3.5
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",  # Выберите нужный движок (GPT-3.5 Turbo или text-davinci-003)
        prompt=user_question,
        max_tokens=1500# Максимальное количество токенов в ответе
    )

    # Выведите ответ
    return (response.choices[0].text.strip())
#API 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
@bot.message_handler(commands=["start"])
def start(message: types.Message):
    bot.send_message(message.chat.id,"Это ChatGpt 3, Что вы хотели бы?")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    user_question = message.text  # Получите текст сообщения
    response = chatgpt(user_question)  # Отправьте текст в функцию chatgpt
    bot.send_message(message.chat.id, response)
bot.polling()





