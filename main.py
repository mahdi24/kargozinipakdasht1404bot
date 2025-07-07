from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")  # ✅ خواندن از متغیر Railway
API_URL = f"https://ble.ir/api/bot{BOT_TOKEN}/sendMessage"

menu_buttons = [["مرخصی", "بازنشستگی"], ["نقل و انتقالات", "طبقه شغلی"], ["ارتباط با ما"]]
menu_responses = {
    "مرخصی": "نوع مرخصی خود را مشخص کنید.",
    "بازنشستگی": "با منابع انسانی تماس بگیرید.",
    "نقل و انتقالات": "فرم شماره ۲ را تکمیل کنید.",
    "طبقه شغلی": "درخواست را به کارگزینی ارسال کنید.",
    "ارتباط با ما": "تماس با: @Amir1068"
}

def send_message(chat_id, text, reply_markup=None):
    data = {"chat_id": chat_id, "text": text}
    if reply_markup:
        data["reply_markup"] = reply_markup
    requests.post(API_URL, json=data)

def send_welcome(chat_id):
    reply_markup = {"keyboard": menu_buttons, "resize_keyboard": True}
    send_message(chat_id, "به ربات خوش آمدید. یکی از گزینه‌ها را انتخاب کنید:", reply_markup)

@app.route("/", methods=["GET"])
def home():
    return "Bot is running"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    print("دریافت شد:", data)
    if not data or "message" not in data:
        return "no message", 200
    message = data["message"]
    chat_id = message["chat"]["id"]
    text = message.get("text", "")
    if text == "/start":
        send_welcome(chat_id)
    elif text in menu_responses:
        send_message(chat_id, menu_responses[text])
    else:
        send_message(chat_id, "لطفاً از دکمه‌ها استفاده کنید.")
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
