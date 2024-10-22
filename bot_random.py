import random
import telebot

bot = telebot.TeleBot("7804472826:AAF1L3rsa1jQctNsql4-4z3lg5wd7WvsHOE")


def get_random(max_value, count):
    return random.sample(range(max_value), min(count, max_value))


def get_lines(filename, ids):
    selected_lines = []
    file = open(filename, encoding='utf-8')
    lines = file.readlines()
    file.close()

    for index in ids:
        if index < len(lines):
            selected_lines.append(lines[index].strip())
    return selected_lines


@bot.message_handler(commands=['getlines'])
def send_random_lines(message):
    command_parts = message.text.split()

    if len(command_parts) > 1:
        count = int(command_parts[1])

        file = open('textfile.txt', encoding='utf-8')
        lines = file.readlines()
        file.close()

        random_indices = get_random(len(lines), count)

        random_lines = get_lines('textfile.txt', random_indices)

        response = ""
        for line in random_lines:
            response += line + "\n"

        bot.send_message(message.chat.id,response.strip())

    else:
        bot.send_message(message.chat.id,
                         "ви вели невірну форму потрібно /getlines <число> наприклад /getlines 3")


bot.polling()
#@kravchykecho_bot окликання на бота