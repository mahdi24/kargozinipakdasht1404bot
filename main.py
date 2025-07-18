from flask import Flask, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = f"https://ble.ir/api/bot{BOT_TOKEN}/sendMessage"

menu_responses = {
    "مرخصی": "📋 لطفاً نوع مرخصی را انتخاب کنید.",
    "بازنشستگی": "📞 برای بازنشستگی با کارگزینی تماس بگیرید.",
    "نقل و انتقالات": "🔄 فرم نقل و انتقالات را تکمیل کنید.",
    "طبقه شغلی": "📚 طبقه شغلی خود را بررسی نمایید.",
    "ارتباط با ما": "🔗 @Amir1068"
}

@app.route("/", methods=["GET"])
def home():
    return "🤖 Bot is running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if not data or "message" not in data:
        return "No message", 200

    message = data["message"]
    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    if text == "/start":
        send_welcome(chat_id)
    elif text in menu_responses:
        send_message(chat_id, menu_responses[text])
    else:
        send_message(chat_id, "❗ لطفاً یکی از گزینه‌ها را انتخاب کنید.")
    return "ok", 200

def send_welcome(chat_id):
    text = "🌟 به ربات کارگزینی خوش آمدید.\nیکی از گزینه‌های زیر را انتخاب کنید:"
    reply_markup = {
        "inline_keyboard": [
            [{"text": "📝 مرخصی", "callback_data": "مرخصی"}],
            [{"text": "📅 بازنشستگی", "callback_data": "بازنشستگی"}],
            [{"text": "🔄 نقل و انتقالات", "callback_data": "نقل و انتقالات"}],
            [{"text": "📚 طبقه شغلی", "callback_data": "طبقه شغلی"}],
            [{"text": "📞 ارتباط با ما", "callback_data": "ارتباط با ما"}],
        ]
    }
    send_message(chat_id, text, reply_markup)

def send_message(chat_id, text, reply_markup=None):
    data = {
        "chat_id": chat_id,
        "text": text
    }
    if reply_markup:
        data["reply_markup"] = reply_markup
    requests.post(API_URL, json=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
