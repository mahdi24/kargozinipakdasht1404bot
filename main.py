from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = f"https://tapi.bale.ai/bot{BOT_TOKEN}"


@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    print(f"📥 داده دریافتی از بله: {data}")
    if not data or "message" not in data:
        return "ok"

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    if text == "/start":
        reply_markup = {
            "inline_keyboard": [
                [{"text": "📄 فرم ثبت‌نام", "url": "https://example.com/form"}],
                [{"text": "📆 برنامه هفتگی", "url": "https://example.com/schedule"}],
                [{"text": "📝 درخواست مرخصی", "url": "https://example.com/leave"}],
                [{"text": "📚 منابع آموزشی", "url": "https://example.com/resources"}],
                [{"text": "📢 اطلاعیه‌ها", "url": "https://example.com/news"}],
                [{"text": "👨‍🏫 لیست مدرسان", "url": "https://example.com/teachers"}],
                [{"text": "🧑‍💼 تماس با پشتیبانی", "url": "https://example.com/support"}],
                [{"text": "📌 آدرس اداره", "url": "https://maps.google.com"}],
                [{"text": "🧾 وضعیت حضور", "url": "https://example.com/attendance"}],
                [{"text": "🔄 بروزرسانی اطلاعات", "url": "https://example.com/update"}],
                [{"text": "❓ سوالات متداول", "url": "https://example.com/faq"}]
            ]
        }

        requests.post(f"{API_URL}/sendMessage", json={
            "chat_id": chat_id,
            "text": "👋 خوش آمدید!\nاز دکمه‌های زیر استفاده کنید:",
            "reply_markup": reply_markup
        })

    return "ok"


@app.route("/", methods=["GET"])
def index():
    return "ربات بله فعال است."


if __name__ == "__main__":
    app.run(debug=True)
gunicorn main:app --bind 0.0.0.0:8080
