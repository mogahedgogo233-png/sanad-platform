import os
import threading
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# --- الإعدادات (تأكد من وضع بياناتك) ---
TOKEN = " 8600729635:AAG8E4oF5dTbBrhKNPsfMDI-FmKWeYrht3E" 
ADMIN_ID = @7061847453 # رقم الآيدي الخاص بك


# إعداد السجلات
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- سيرفر الـ Health Check لـ Render ---
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is Running")

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

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
