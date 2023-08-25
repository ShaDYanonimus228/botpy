#6589678614:AAEKwUHM-Z52EdphhU5Pq9OA6f7z5agQA4Y
from datetime import datetime
from pyrogram import*
from api import*
import time
my_chat_id = 1524610051
now = datetime.now()
current_time = now.strftime("%H:%M")

api_id = 20570867
api_hash = '0e123778ea491f4425b56216ae022434'

with Client("my_account", api_id, api_hash) as app:
    while True:
        time.sleep(1)
        print(current_time)
        if current_time == current_time:  # Выставляете ваше время
            print('pass')
            app.send_message('@cryptoivests', "Разбуди меня,пожалуйста")
            app.send_message('@cryptoivests', "Разбуди меня,пожалуйста")
            app.send_message('@cryptoivests', "Разбуди меня,пожалуйста")



