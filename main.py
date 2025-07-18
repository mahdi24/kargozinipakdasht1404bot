from flask import Flask, request
import requests
import os

app = Flask(__name__)

# اطلاعات توکن و URL
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = f"https://tapi.bale.ai/bot{BOT_TOKEN}"

@app.route('/', methods=["POST"])
def webhook():
    data = request.json

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            send_message(chat_id, "به ربات خوش آمدید!", [
                [{"text": "💼 اطلاعات کارگزینی", "callback_data": "info"}],
                [{"text": "📅 تقویم آموزشی", "callback_data": "calendar"}],
                [{"text": "📞 تماس با ما", "url": "https://example.com/contact"}]
            ])
    
    elif "callback_query" in data:
        query = data["callback_query"]
        chat_id = query["message"]["chat"]["id"]
        data_id = query["data"]

        if data_id == "info":
            send_message(chat_id, "🔍 اطلاعات کامل کارگزینی را اینجا مشاهده کنید.")
        elif data_id == "calendar":
            send_message(chat_id, "📅 تقویم آموزشی ترم جدید به زودی بارگذاری خواهد شد.")

    return "ok"

def send_message(chat_id, text, buttons=None):
    payload = {
        "chat_id": chat_id,
        "text": text,
        "reply_markup": {
            "inline_keyboard": buttons
        } if buttons else None
    }
    headers = {'Content-Type': 'application/json'}
    requests.post(f"{API_URL}/sendMessage", json=payload, headers=headers)

if __name__ == "__main__":
    app.run()
