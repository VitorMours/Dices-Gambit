import logging
from datetime import date, datetime

class Logging:
    logging.basicConfig(filename="system.log", encoding="utf-8")



def create_log(action):
    date_time_info = f"{date.today()} {datetime.now().strftime('%H:%M:%S')}" 
    

    return log

print(date.today())
logging.warning('whatch out!')



print(create_log())


















