
from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "1004988187:QrErRwdnhUaKHIXjFKGxQxMHe60WUrqeGnMQz3y6"
API_URL = f"https://ble.ir/api/bot{BOT_TOKEN}/sendMessage"
@app.route("/", methods=["POST"])
def webhook():
    update = request.get_json()

    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")

        if text == "/start":
            send_welcome(chat_id)

    return {"ok": True}

def send_welcome(chat_id):
    data = {
        "chat_id": chat_id,
        "text": "به ربات کارگزینی خوش آمدید 🌟\nلطفاً یکی از گزینه‌ها را انتخاب کنید:",
        "reply_markup": {
            "inline_keyboard": [
                [{"text": "📝 فرم ثبت‌نام", "url": "https://example.com/form"}],
                [{"text": "📞 تماس با ما", "callback_data": "contact"}]
            ]
        }
    }
    requests.post(f"{API_URL}/sendMessage", json=data)

menu_buttons = [
    ["مرخصی", "بازنشستگی"],
    ["نقل و انتقالات", "طبقه شغلی"],
    ["رتبه شغلی", "بازخرید"],
    ["استعفا", "تخلفات"],
    ["گواهی اشتغال به کار", "انتصابات"],
    ["ارتباط با ما"]
]

menu_responses = {
    "مرخصی": "لطفاً نوع مرخصی خود را مشخص کرده و فرم مربوطه را ارسال نمایید.",
    "بازنشستگی": "جهت امور بازنشستگی با بخش منابع انسانی تماس بگیرید.",
    "نقل و انتقالات": "برای نقل و انتقالات، فرم شماره ۲ را تکمیل نمایید.",
    "طبقه شغلی": "درخواست بررسی طبقه شغلی را به کارگزینی ارسال کنید.",
    "رتبه شغلی": "اطلاعات مربوط به رتبه شغلی به‌زودی اعلام می‌شود.",
    "بازخرید": "برای بازخرید خدمت، فرم رسمی درخواست را تکمیل نمایید.",
    "استعفا": "به زودی بارگذاری خواهد شد. از صبر و شکیبایی شما سپاسگزاریم.",
    "تخلفات": "به زودی بارگذاری خواهد شد. از صبر و شکیبایی شما سپاسگزاریم.",
    "گواهی اشتغال به کار": "به زودی بارگذاری خواهد شد. از صبر و شکیبایی شما سپاسگزاریم.",
    "انتصابات": "تغییرات انتصابات در سامانه ثبت می‌شود.",
    "ارتباط با ما": "ارتباط با مسئول کارگزینی: @Amir1068\nارتباط با مدیر ربات: @teacher141072"
}

def send_message(chat_id, text, reply_markup=None):
    data = {"chat_id": chat_id, "text": text}
    if reply_markup:
        data["reply_markup"] = reply_markup
    requests.post(API_URL, json=data)

def send_welcome(chat_id):
    reply_markup = {"keyboard": menu_buttons, "resize_keyboard": True}
    welcome_text = "به بازوی کارگزینی اداره آموزش و پرورش پاکدشت خوش آمدید.\nلطفاً یکی از گزینه‌ها را انتخاب کنید:"
    send_message(chat_id, welcome_text, reply_markup)

@app.route("/", methods=["GET"])
def home():
    return "Bot is running"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
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
        send_message(chat_id, "لطفاً از دکمه‌های موجود استفاده کنید.")

    return "ok", 200
