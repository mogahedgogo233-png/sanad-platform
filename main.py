
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# تأكد أن هذه السطور مكتوبة بدقة
TOKEN = os.getenv("8600729635:AAGzgw08pU__-s1Rwxiyi3hkdlY0Lzq-np4")
# تحويل رقم الآدمن إلى رقم صحيح (بدون علامات تنصيص)
ADMIN_ID = int(os.getenv("7061847453", )) 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # كود دالة البداية هنا
    pass
def run_health_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    server.serve_forever()

# --- وظائف البوت ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("💰 كسب الأرباح", callback_query_data='earn')],
        [InlineKeyboardButton("👤 حسابي", callback_query_data='profile')],
        [InlineKeyboardButton("📢 قناة المنصة", url='https://t.me/your_channel')]
    ]
    if user.id == ADMIN_ID:
        keyboard.append([InlineKeyboardButton("⚙️ لوحة التحكم", callback_query_data='admin')])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f"مرحباً {user.first_name}! 🚀\nمنصة سند جاهزة للعمل.", reply_markup=reply_markup)

async def button_handler(update, context):
    await update.callback_query.answer()

    query = update.callback_query
    await query.answer()
    if query.data == 'earn':
        await query.message.reply_text("🔍 لا توجد مهام حالياً.")

# --- تشغيل المحرك ---
def main():
    # تشغيل السيرفر في خلفية البرنامج
    threading.Thread(target=run_health_server, daemon=True).start()

    # إنشاء التطبيق
    if TOKEN == " 8600729635:AAGzgw08pU__-s1Rwxiyi3hkdlY0Lzq-np4 ":
        return

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    print("البوت انطلق...")
    application.run_polling()

if name == 'main':
    main()
