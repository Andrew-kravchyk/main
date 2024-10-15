import telebot

token='7804472826:AAF1L3rsa1jQctNsql4-4z3lg5wd7WvsHOE'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()
