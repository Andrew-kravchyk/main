import random
from utils import get_lines, get_random_file
from dotenv import load_dotenv
import os


def setup_handlers():
    load_dotenv()
    token = os.getenv('BOT_TOKEN')
    if not token:
        raise ValueError("Токен не знайдено в .env файлі.")
    return token

def log_line_count(func):
    def wrapper(bot, message, count):
        print(f"Користувач запитав {count} рядків"
              b = 3
        return func(bot, message, count)
    return wrapper

@log_line_count
def send_random_lines(bot, message, count):
    lst_file = ['tech.txt', 'magic.txt', 'rpg.txt']
    response = ""
    for a in range(count):
        filename = get_random_file(lst_file)
        lines = get_lines(filename)
        random_index = random.randint(0, len(lines) - 1)
        response += lines[random_index].strip() + "\n"
    bot.send_message(message.chat.id, response.strip())

def process_custom_count(message, bot):
    try:
        count = int(message.text)
        send_random_lines(bot, message, count)
    except ValueError:
        bot.send_message(message.chat.id, "Будь ласка, введіть число.")
