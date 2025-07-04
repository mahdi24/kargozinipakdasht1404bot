@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = request.get_json()
    print("پیام دریافت‌شده:", update)

    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")

        if text == "/start":
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

    return "ok", 200
