import requests
import os

# 📦 بارگذاری اطلاعات از متغیرهای محیطی
BOT_TOKEN = os.getenv('BOT_TOKEN')
DOMAIN_URL = os.getenv('DOMAIN_URL')  # مثل https://your-app-name.onrender.com

WEBHOOK_URL = f'{DOMAIN_URL}/webhook'
SET_WEBHOOK_URL = f'https://tapi.bale.ai/bot{BOT_TOKEN}/setWebhook'
SEND_MESSAGE_URL = f'https://tapi.bale.ai/bot{BOT_TOKEN}/sendMessage'

def set_webhook():
    response = requests.post(SET_WEBHOOK_URL, json={'url': WEBHOOK_URL})
    print("🔗 نتیجه ثبت webhook:", response.json())

def send_test_message(chat_id):
    payload = {
        'chat_id': chat_id,
        'text': '✅ Webhook با موفقیت ثبت شد.'
    }
    response = requests.post(SEND_MESSAGE_URL, json=payload)
    print("📨 نتیجه پیام تست:", response.json())

if __name__ == "__main__":
