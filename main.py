from flask import Flask, request
import requests
import os

app = Flask(__name__)
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = f"https://tapi.bale.ai/bot{BOT_TOKEN}"

@app.route("/")
def home():
    return "OK", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("دریافت شد:", data)

    if not data or "message" not in data:
        return "no message", 200

    message = data["message"]
    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    if text == "/start":
        send_message(chat_id, "سلام! به ربات خوش اومدی 🌟", buttons=True)

    return "ok", 200

def send_message(chat_id, text, buttons=False):
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }

    if buttons:
        payload["reply_markup"] = {
            "inline_keyboard": [
                [{"text": "دکمه ۱", "callback_data": "btn1"}],
                [{"text": "دکمه ۲", "callback_data": "btn2"}]
            ]
        }

    requests.post(f"{API_URL}/sendMessage", json=payload)

if __name__ == "__main__":
    app.run()
