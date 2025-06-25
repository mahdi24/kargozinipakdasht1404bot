from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running."

@app.route('/<token>', methods=['POST'])
def bot(token):
    update = request.get_json()
    message = update.get('message', {}).get('text', '')
    chat_id = update.get('message', {}).get('chat', {}).get('id', '')

    if message == "/start":
        reply = "به بازوی کارگزینی اداره آموزش و پرورش پاکدشت خوش آمدید. لطفاً یکی از گزینه‌های زیر را انتخاب کنید:"
    elif message in ["مرخصی", "بازنشستگی", "نقل و انتقالات", "طبقه شغلی", "رتبه شغلی", "بازخرید", "انتصابات"]:
        reply = f"اطلاعات مربوط به {message} در حال بارگذاری است..."
    elif message in ["استعفا", "تخلفات", "گواهی اشتغال به کار"]:
        reply = "به زودی بارگذاری خواهد شد. از صبر و شکیبایی شما سپاسگزاریم."
    elif message == "ارتباط با ما":
        reply = "مسئول کارگزینی: @Amir1068\nمدیریت ارتباطات: @teacher141072"
    else:
        reply = "گزینه نامعتبر است."

    return {"method": "sendMessage", "chat_id": chat_id, "text": reply}

if __name__ == '__main__':
    app.run()
