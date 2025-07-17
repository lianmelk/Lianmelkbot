
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from flask import Flask
from threading import Thread

# ربات توکن
TOKEN = "7596222665:AAF1ew5t9IJqgih8M8HVOmmx1tD0sUeBTaA"

# Flask سرور برای آنلاین نگه‌داشتن ربات
app = Flask('')

@app.route('/')
def home():
    return "ربات لیان فعال است ✅"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()

# دستور start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🗺 مشاهده روی نقشه", "🏘 خرید و فروش"],
        ["📞 تماس با ما", "📍 موقعیت دفتر"],
        ["🔎 جستجو", "💬 درباره ما"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("به ربات مشاورین املاک لیان خوش آمدید! 👋", reply_markup=reply_markup)

# هندلر پیام‌ها
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    response = {
        "🗺 مشاهده روی نقشه": "📍 آدرس روی نقشه: https://goo.gl/maps/wcGRDrqGJb9hZzYJ8",
        "🏘 خرید و فروش": "لیست املاک خرید و فروش: https://lianmelk.com",
        "📞 تماس با ما": "شماره تماس:
09142842426
04137424181",
        "📍 موقعیت دفتر": "آدرس:
مراغه، ولیعصر، خیابان ۱۲ بهمن، نبش کوچه شکیبا",
        "💬 درباره ما": "مشاورین املاک لیان با سال‌ها تجربه در زمینه خرید، فروش، رهن و اجاره...",
        "🔎 جستجو": "برای جستجوی ملک به وب‌سایت ما مراجعه کنید:
https://lianmelk.com"
    }.get(text, "لطفاً یکی از گزینه‌های منو را انتخاب کنید ✅")

    await update.message.reply_text(response)

# اجرای ربات
app_telegram = ApplicationBuilder().token(TOKEN).build()
app_telegram.add_handler(CommandHandler("start", start))
app_telegram.add_handler(MessageHandler(filters.TEXT, handle_message))
app_telegram.run_polling()
