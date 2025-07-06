from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "توکن_جدید_تو"  # ⚠️ توکن واقعی رباتتو بذار اینجا

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = request.get_json()
    print("پیام دریافت شد:", update)

    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        message_text = update["message"].get("text", "")
        reply = f"شما گفتید: {message_text}"

        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": chat_id, "text": reply}
        )

    return "", 200

@app.route("/")
def home():
    return "ربات فعاله ✅", 200
