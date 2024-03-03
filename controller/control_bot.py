#control_bot.py
from bot.bot import Bot

bot = Bot()

def start_bot(query):
    try:
        bot.open_page()
        bot.search(query)
    except Exception as e:
        print(e)
