import telebot
import os
import time

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

if __name__ == "__main__":
    print("Бот запущен...")
    while True:
        try:
            bot.infinity_polling(timeout=60)
        except Exception as e:
            print(f"Ошибка: {e}")
            time.sleep(15)
