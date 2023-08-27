#6589678614:AAEKwUHM-Z52EdphhU5Pq9OA6f7z5agQA4Y
from datetime import datetime
from pyrogram import*
from api import*
import time
my_chat_id = 1524610051

api_id = 20570867
api_hash = '0e123778ea491f4425b56216ae022434'

with Client("my_account", api_id, api_hash) as app:
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        time.sleep(1)
        print(current_time)
        if current_time == '10:00':  # Выставляете ваше время
            print('pass')
            app.send_message('@banan123455', "Разбуди меня,пожалуйста")
            app.send_message('@banan123455', "Разбуди меня,пожалуйста")
            app.send_message('@banan123455', "Разбуди меня,пожалуйста")



