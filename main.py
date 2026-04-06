import telebot
from flask import Flask, request
import os

TOKEN = "8411810943:AAHKjdJ9IVCpJ6tibDd6fwweQZFnq8Nw1kk"
CHANNEL_LINK = "https://t.me/+RCqrXBwVCi1kNTg0"
CHAT_LINK = "https://t.me/+YybtW77iiD84ZmYy"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    text = f"""⚠️ Чтобы воспользоваться сн@сером, подпишись на:

📢 Канал: {CHANNEL_LINK}
💬 Чат: {CHAT_LINK}

✅ После подписки нажми /start снова"""
    
    bot.send_message(message.chat.id, text)

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

if __name__ == '__main__':
    bot.remove_webhook()
    WEBHOOK_URL = os.getenv('RAILWAY_PUBLIC_DOMAIN', '')
    if WEBHOOK_URL:
        bot.set_webhook(url=f'https://{WEBHOOK_URL}/{TOKEN}')
        print(f'Webhook set: https://{WEBHOOK_URL}/{TOKEN}')
    
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
