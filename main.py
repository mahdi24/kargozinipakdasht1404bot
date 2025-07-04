from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "1004988187:QrErRwdnhUaKHIXjFKGxQxMHe60WUrqeGnMQz3y6"

@app.route(f"/{BOT_TOKEN}", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return "Bot is running.", 200

    data = request.get_json()
    if not data:
        return "no data", 400

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            reply_markup = {
    "keyboard": [
        [{"text": "مرخصی"}, {"text": "بازنشستگی"}],
        [{"text": "طبقه شغلی"}, {"text": "رتبه شغلی"}],
        [{"text": "استعفا"}, {"text": "تخلفات"}],
        [{"text": "انتصابات"}, {"text": "ارتباط با ما"}]
    ],
    "resize_keyboard": True,
    "one_time_keyboard": False
}
            }
            send_message(chat_id, "به بازوی کارگزینی اداره آموزش و پرورش پاکدشت خوش آمدید", reply_markup)
        else:
            send_message(chat_id, "دستور نامشخص است.")
    else:
        print("پیام نامعتبر دریافت شد:", data)

    return "ok", 200

def send_message(chat_id, text, reply_markup=None):
    url = f"https://ble.ir/api/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    if reply_markup:
        payload["reply_markup"] = reply_markup
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
