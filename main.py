from flask import Flask, request
import requests

app = Flask(__name__)

# 🔐 توکن ربات را اینجا وارد کن
BOT_TOKEN = "1004988187:F2UsGTol6UD4wRdE8KolcxNDll4kWt78aXAacke6"

# 🛣 مسیر مخصوص وب‌هوک
WEBHOOK_PATH = f"/{BOT_TOKEN}"

@app.route("/", methods=["GET"])
def home():
    return "ربات تلگرام فعال است", 200

@app.route(WEBHOOK_PATH, methods=["POST"])
def webhook():
    update = request.get_json()
    print("📩 پیام دریافت‌شده:", update)

    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")

        # پاسخ ساده
        send_message(chat_id, f"شما گفتید: {text}")

    return "OK", 200

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    # پورت 8000 طبق استاندارد Railway
    app.run(host="0.0.0.0", port=8000)
