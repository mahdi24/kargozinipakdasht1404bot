📁 main.py

import os from flask import Flask, request import requests from dotenv import load_dotenv

بارگذاری متغیرهای محیطی از فایل .env

load_dotenv()

app = Flask(name)

دریافت توکن از متغیر محیطی

BOT_TOKEN = os.getenv("BOT_TOKEN") API_URL = f"https://ble.ir/api/bot{BOT_TOKEN}/sendMessage"

دکمه‌های منوی اصلی

menu_buttons = [ ["مرخصی", "بازنشستگی"], ["نقل و انتقالات", "طبقه شغلی"], ["رتبه شغلی", "بازخرید"], ["استعفا", "تخلفات"], ["گواهی اشتغال به کار", "انتصابات"], ["ارتباط با ما"] ]

menu_responses = { "مرخصی": "لطفاً نوع مرخصی خود را مشخص کرده و فرم مربوطه را ارسال نمایید.", "بازنشستگی": "جهت امور بازنشستگی با بخش منابع انسانی تماس بگیرید.", "نقل و انتقالات": "برای نقل و انتقالات، فرم شماره ۲ را تکمیل نمایید.", "طبقه شغلی": "درخواست بررسی طبقه شغلی را به کارگزینی ارسال کنید.", "رتبه شغلی": "اطلاعات مربوط به رتبه شغلی به‌زودی اعلام می‌شود.", "بازخرید": "برای بازخرید خدمت، فرم رسمی درخواست را تکمیل نمایید.", "استعفا": "به زودی بارگذاری خواهد شد.", "تخلفات": "به زودی بارگذاری خواهد شد.", "گواهی اشتغال به کار": "به زودی بارگذاری خواهد شد.", "انتصابات": "تغییرات انتصابات در سامانه ثبت می‌شود.", "ارتباط با ما": "ارتباط با مسئول کارگزینی: @Amir1068\nارتباط با مدیر ربات: @teacher141072" }

def send_message(chat_id, text, reply_markup=None): data = {"chat_id": chat_id, "text": text} if reply_markup: data["reply_markup"] = reply_markup requests.post(API_URL, json=data)

def send_welcome(chat_id): reply_markup = {"keyboard": menu_buttons, "resize_keyboard": True} welcome_text = "به بازوی کارگزینی اداره آموزش و پرورش پاکدشت خوش آمدید.\nلطفاً یکی از گزینه‌ها را انتخاب کنید:" send_message(chat_id, welcome_text, reply_markup)

@app.route("/") def home(): return "Bot is running."

@app.route(f"/{BOT_TOKEN}", methods=["POST"]) def

