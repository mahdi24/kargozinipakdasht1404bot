from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/1004988187:QrErRwdnhUaKHIXjFKGxQxMHe60WUrqeGnMQz3y6', methods=["POST"])
def webhook():
    data = request.get_json()
    print("🔔 پیام دریافت شد از بله:")
    print(data)
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
