import telebot

bot = telebot.TeleBot("8021362694:AAGum8YyJEuojz1ylBRfVIxBSMPgWd5g0es")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот - повторюшка. Напиши что-нибудь!")

@bot.message_handler(commands=['repeat', 'hello'])
def repeat_message(message):
    bot.reply_to(message, 'Теперь я буду повторять за тобой!')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
