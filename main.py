from flask import Flask, request
import requests

app = Flask(__name__)

# توکن ربات شما
BOT_TOKEN = "1004988187:F2UsGTol6UD4wRdE8KolcxNDll4kWt78aXAacke6"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = request.get_json()
    print("پیام دریافت‌شده:", update)

    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")

        # پاسخ ساده به پیام دریافتی
        response_text = "سلام! پیام شما دریافت شد ✅"

        requests.post(
            f"https://ble.shad.ir/api/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": chat_id, "text": response_text}
        )

    return "ok"

@app.route("/", methods=["GET"])
def index():
    return "ربات فعال است ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
