from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "1004988187:QrErRwdnhUaKHIXjFKGxQxMHe60WUrqeGnMQz3y6"
BLE_API_URL = f"https://ble.ir/api/bot{BOT_TOKEN}/sendMessage"

@app.route("/")
def home():
    return "Bot is running"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    if text == "/start":
        send_menu(chat_id)
    elif text in menu_responses:
        response = menu_responses[text]
        send_message(chat_id, response)
    else:
        send_message(chat_id, "لطفاً از دکمه‌های موجود استفاده کنید.")

    return "ok"

def send_message(chat_id, text, reply_markup=None):
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    if reply_markup:
        payload["reply_markup"] = reply_markup
    requests.post(BLE_API_URL, json=payload)

def send_menu(chat_id):
    buttons = [
        ["مرخصی", "بازنشستگی"],
        ["نقل و انتقالات", "طبقه شغلی"],
        ["رتبه شغلی", "بازخرید"],
        ["استعفا", "تخلفات"],
        ["گواهی اشتغال به کار", "انتصابات"],
        ["ارتباط با ما"]
    ]
    reply_markup = {"keyboard": buttons, "resize_keyboard": True}
    send_message(chat_id, "به بازوی کارگزینی اداره آموزش و پرورش پاکدشت خوش آمدید.\nلطفاً یکی از گزینه‌ها را انتخاب کنید:", reply_markup)

menu_responses = {
    "مرخصی": "لطفاً نوع مرخصی خود را مشخص کرده و فرم مربوطه را ارسال نمایید.",
    "بازنشستگی": "جهت امور بازنشستگی با بخش منابع انسانی تماس بگیرید.",
    "نقل و انتقالات": "برای نقل و انتقالات، فرم شماره ۲ را تکمیل نمایید.",
    "طبقه شغلی": "درخواست بررسی طبقه شغلی را به کارگزینی ارسال کنید.",
    "رتبه شغلی": "اطلاعات مربوط به رتبه شغلی به‌زودی اعلام می‌شود.",
    "بازخرید": "برای بازخرید خدمت، فرم رسمی درخواست را تکمیل نمایید.",
    "استعفا": "به زودی بارگذاری خواهد شد از صبر و شکیبایی شما سپاسگزاریم.",
    "تخلفات": "به زودی بارگذاری خواهد شد از صبر و شکیبایی شما سپاسگزاریم.",
    "گواهی اشتغال به کار": "به زودی بارگذاری خواهد شد از صبر و شکیبایی شما سپاسگزاریم.",
    "انتصابات": "تغییرات انتصابات در سامانه ثبت می‌شود.",
    "ارتباط با ما": "ارتباط با مسئول کارگزینی: @Amir1068\nارتباط با مدیر ربات: @teacher141072"
}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
