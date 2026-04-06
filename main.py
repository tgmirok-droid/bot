import telebot

# ЗАМЕНИТЕ НА ВАШ ТОКЕН
TOKEN = "8411810943:AAHKjdJ9IVCpJ6tibDd6fwweQZFnq8Nw1kk"

CHANNEL_LINK = "https://t.me/+RCqrXBwVCi1kNTg0"
CHAT_LINK = "https://t.me/+YybtW77iiD84ZmYy"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    text = f"""⚠️ Чтобы воспользоваться сн@сером, подпишись на:

📢 Канал: {CHANNEL_LINK}
💬 Чат: {CHAT_LINK}

✅ После подписки нажми /start снова"""
    
    bot.send_message(message.chat.id, text)

print("Бот запущен...")
bot.infinity_polling()