from flask import Flask, request
import requests

app = Flask(name)
BOT_TOKEN = "1004988187:QrErRwdnhUaKHIXjFKGxQxMHe60WUrqeGnMQz3y6"

@app.route(f"/{BOT_TOKEN}", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return "Bot is running.", 200

    update = request.get_json()
    print("دریافت شد:", update)

    if update and "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")

        if text == "/start" or text == "شروع" or text == "start":
            reply_markup = {
                "keyboard": [
                    ["مرخصی", "بازنشستگی", "نقل و انتقالات"],
                    ["طبقه شغلی", "رتبه شغلی", "بازخرید"],
                    ["استعفا", "تخلفات", "گواهی اشتغال به کار"],
                    ["انتصابات", "ارتباط با ما"]
                ],
                "resize_keyboard": True,
                "one_time_keyboard": False
            }
            send_message(chat_id, "به بازوی کارگزینی اداره آموزش و پرورش پاکدشت خوش آمدید", reply_markup)
        else:
            send_message(chat_id, "دستور نامشخص است.")
    else:
        print("پیام نامعتبر دریافت شد:", update)

    return "ok", 200

def send_message(chat_id, text, reply_markup=None):
    url = f"https://ble.ir/api/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    if reply_markup:
        payload["reply_markup"] = reply_markup

    response = requests.post(url, json=payload)
    print("ارسال پیام:", response.status_code, response.text)

if name == "main":
    app.run(host="0.0.0.0", port=8000)
