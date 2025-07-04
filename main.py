from flask import Flask, request
import requests

app = Flask(name)

# توکن ربات بله
BOT_TOKEN = "1004988187:QrErRwdnhUaKHIXjFKGxQxMHe60WUrqeGnMQz3y6"

@app.route("/")
def home():
    return "ربات فعال است ✅", 200

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = request.get_json()

    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")

        if text == "/start":
            send_message(chat_id, "به بازوی کارگزینی اداره آموزش و پرورش پاکدشت خوش آمدید")
        else:
            send_message(chat_id, "دستور نامشخص است.")

    return "ok", 200

def send_message(chat_id, text):
    url = f"https://ble.ir/api/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if name == "main":
    app.run(host="0.0.0.0", port=8000)
