import os
import threading
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# 1. إعداد Flask لفتح "منفذ" وإرضاء Render
app = Flask(name)

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    # Render يمرر المنفذ تلقائياً عبر متغير بيئة يسمى PORT
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# 2. إعدادات البوت وأمر Start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    
    # رسالة الترحيب مع قناتك (مزاجك رايق)
    welcome_text = (
        f"أهلاً بك يا {user_name} في بوت التحميل 🚀\n\n"
        "للاستمرار، يرجى الاشتراك في قناة البوت الرسمية أولاً."
    )
    
    keyboard = [
        [InlineKeyboardButton("قناة مزاجك رايق 🎵", url="https://t.me/+QOUIea_dVt8zMzk0")],
        [InlineKeyboardButton("تم الاشتراك ✅", callback_data='check_sub')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# 3. تشغيل كل شيء معاً
def main():
    # تشغيل Flask في خيط (Thread) منفصل
    threading.Thread(target=run_flask, daemon=True).start()

    # وضع التوكن الخاص بك
    TOKEN = "8600729635:AAGzgw08pU__-s1Rwxiyi3hkdlY0Lzq-np4"
    
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    print("البوت والسيرفر يعملان...")
    application.run_polling()

if __name__ == '__main__':
    main()


