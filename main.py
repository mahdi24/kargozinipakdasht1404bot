from flask import Flask, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")  # توکن ربات
API_URL = "https://tapi.bale.ai/bot" + BOT_TOKEN
app = Flask(__name__)


def send_message(chat_id, text, buttons=None):
    payload = {
        "chat_id": chat_id,
        "text": text,
        "reply_markup": {
            "inline_keyboard": buttons or []
        }
    }
    response = requests.post(f"{API_URL}/sendMessage", json=payload)
    print("Send message response:", response.text)


@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    print("Update received:", data)

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            buttons = [
                [{"text": "📄 درباره ما", "callback_data": "about"}],
                [{"text": "🗓 تماس با ما", "callback_data": "contact"}],
            ]
            send_message(chat_id, "به ربات خوش آمدید! یکی از گزینه‌ها را انتخاب کنید:", buttons)

    elif "callback_query" in data:
        query = data["callback_query"]
        chat_id = query["message"]["chat"]["id"]
        data_text = query["data"]

        if data_text == "about":
            send_message(chat_id, "ما ربات رسمی کارگزینی اداره آموزش‌وپرورش پاکدشت هستیم.")

        elif data_text == "contact":
            send_message(chat_id, "برای تماس با ما به شماره ۰۹۱۲xxxxxxx پیام دهید.")

    return "ok", 200


@app.route("/", methods=["GET"])
def index():
    return "ربات فعال است", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
