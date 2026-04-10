import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --- بياناتك ---
BOT_TOKEN = "8600729635:AAGzgw08pU__-s1Rwxiyi3hkdlY0Lzq-np4" 
ADMIN_ID = 7061847453 # ضع رقمك هنا

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"أهلاً بك! البوت يعمل بنجاح الآن.")

def main():
    # بناء التطبيق
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # إضافة الأوامر
    application.add_handler(CommandHandler("start", start))
    
    print("البوت بدأ العمل بنجاح...")
    
    # هذه الطريقة هي الأفضل لمنع أخطاء الـ Event Loop في Render
    application.run_polling(stop_signals=None)

if __name__ == '__main__':
    main()


