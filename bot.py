import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "Assalomu alaykum! 🛍 New Bukhara Shop do‘koniga xush kelibsiz!",
        reply_markup=menu()
    )

def menu():
    markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    markup.row("🛍 Товары👑", "🚀 Support")
    markup.row("💳 Карта")
    return markup

bot.infinity_polling()
