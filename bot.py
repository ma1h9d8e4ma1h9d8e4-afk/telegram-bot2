import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# التوكن سيتم أخذه من المتغير البيئي TOKEN
TOKEN = os.environ.get("8445342473:AAGeKZXgqeWlQ8GtxeBg5w_F7z35bBvcNro")

# قائمة الأزرار
keyboard = [
    ["من أجل الرزق"],
    ["من أجل الحسد"],
    ["من أجل الإنجاب"],
    ["من أجل التوافق"]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# الرد على /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "اختر الخدمة المطلوبة من القائمة أدناه:",
        reply_markup=reply_markup
    )

# الرد على اختيار أي زر
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = (
        "🔹 تم استلام اختيارك.\n\n"
        "يرجى شحن مبلغ **٥٠٠٠٠ ل.س** عبر سيرتيل كاش.\n"
        "📌 بعد التحويل أرسل **رقم عملية التحويل** للتأكيد.\n"
        "⚠️ بعد الإرسال يمكنك التواصل مع الشيخ.\n"
        "ملاحظة: لسنا مسؤولين عن فقدان الأموال بدون رقم عملية التحويل."
    )
    await update.message.reply_text(response, parse_mode="Markdown")

# إعداد التطبيق
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

print("Bot is running...")
app.run_polling()
