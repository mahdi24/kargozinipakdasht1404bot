from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")  # مقدار از .env یا مستقیم
API_URL = f"https://ble.ir/api/bot{BOT_TOKEN}/sendMessage"

# آدرس سرور لیارا (برای forward پیام)
LIARA_URL = os.getenv("LIARA_FORWARD_URL")  # مثلاً: https://kargozinipakdasht144bot.liara.run

@app.route("/", methods=["GET"])
def home():
    return "Runflare bot is running"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()

    # → ارسال پیام به لیارا (اگر تعریف شده باشد)
    if LIARA_URL:
        try:
            requests.post(f"{LIARA_URL}/{BOT_TOKEN}", json=data)
        except Exception as e:
            print("خطا در ارسال به لیارا:", e)

    # ادامه پردازش پیام
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


def send_message(chat_id, text, reply_markup=None):
    data = {"chat_id": chat_id, "text": text}
    if reply_markup:
        data["reply_markup"] = reply_markup
    requests.post(API_URL, json=data)

def send_welcome(chat_id):
    reply_markup = {"keyboard": menu_buttons, "resize_keyboard": True}
    welcome_text = "به بازوی کارگزینی پاکدشت خوش آمدید.\nیکی از گزینه‌ها را انتخاب کنید:"
    send_message(chat_id, welcome_text, reply_markup)


menu_buttons = [
    ["مرخصی", "بازنشستگی"],
    ["نقل و انتقالات", "طبقه شغلی"],
    ["ارتباط با ما"]
]

menu_responses = {
    "مرخصی": "لطفاً نوع مرخصی را مشخص کنید.",
    "بازنشستگی": "با منابع انسانی تماس بگیرید.",
    "نقل و انتقالات": "فرم ۲ را تکمیل نمایید.",
    "طبقه شغلی": "به کارگزینی مراجعه نمایید.",
    "ارتباط با ما": "ارتباط با مدیر: @Amir1068"
}
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
