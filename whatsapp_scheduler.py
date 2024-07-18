import pywhatkit as kit
import time
from datetime import datetime, timedelta
import schedule

# Замените 'номер_телефона' на номер получателя в формате 'страна+номер' (например, '+79991112233')
phone_number = '+79023996920'
message = 'Авто сообщение котое будет отправляться в 11:25 11:26 11:27 11:24 '

def send_message():
    current_time = datetime.now()
    # Установим отправку сообщения через минуту после вызова функции
    send_time = current_time + timedelta(minutes=1)
    kit.sendwhatmsg(phone_number, message, send_time.hour, send_time.minute)
    print(f"Сообщение отправлено в {send_time.strftime('%H:%M')}")

# Планируем отправку сообщений в нужное время (например, в 9:00, 13:00, 17:00, 21:00)
schedule.every().day.at("12:20").do(send_message)
schedule.every().day.at("12:30").do(send_message)
schedule.every().day.at("12:40").do(send_message)
schedule.every().day.at("11:24").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
