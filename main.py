import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --- ضع بياناتك هنا مباشرة ---
BOT_TOKEN = "8600729635:AAGzgw08pU__-s1Rwxiyi3hkdlY0Lzq-np4" #
ADMIN_ID = 7061847452 #

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id == ADMIN_ID:
        await update.message.reply_text("أهلاً بك يا مدير النظام (سند). تم التشغيل بنجاح!")
    else:
        await update.message.reply_text("مرحباً بك! البوت يعمل الآن.")

async def main():
    # بناء التطبيق
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # إضافة الأوامر
    application.add_handler(CommandHandler("start", start))
    
    print("البوت بدأ العمل بنجاح...")
    await application.run_polling()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Error: {e}")

