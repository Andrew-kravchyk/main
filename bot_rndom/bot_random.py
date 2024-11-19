from telebot import TeleBot, types
from handlers import setup_handlers, send_random_lines, process_custom_count

def main():
    bot = TeleBot(setup_handlers())

    @bot.message_handler(commands=['getlines'])
    def choose_line_count(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.add('10', '20', '30', 'Ввести іншу кількість')
        bot.send_message(message.chat.id, "Виберіть кількість рядків або введіть іншу кількість:", reply_markup=markup)


    @bot.message_handler(content_types=['text'])
    def handle_line_count(message):
        if message.text in ['10', '20', '30']:
            count = int(message.text)
            send_random_lines(bot, message, count)
        elif message.text == 'Ввести іншу кількість':
            bot.send_message(message.chat.id, "Введіть кількість рядків (число):")
            bot.register_next_step_handler(message, process_custom_count, bot)

    bot.polling()

if __name__ == "__main__":
    main()
