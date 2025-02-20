import telebot
    
    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("8021362694:AAGum8YyJEuojz1ylBRfVIxBSMPgWd5g0es")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот - повторюшка. Напиши что-нибудь!")
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.polling().py
