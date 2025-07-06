from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "توکن_جدید_اینجا"
WEBHOOK_PATH = f"/{BOT_TOKEN}"

@app.route(WEBHOOK_PATH, methods=["POST"])
def webhook():
    update = request.get_json()
    print("پیام دریافت‌شده:", update)

    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"]["text"]

        reply = f"شما گفتید: {text}"
        send_message(chat_id, reply)

    return "ok", 200

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8000)
