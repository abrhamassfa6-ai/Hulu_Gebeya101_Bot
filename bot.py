from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8921898109:AAEwUgn413G1vPujEbnV5qUecTyPOvBT7jE"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🛴 Scooter"],
        ["🛹 Hoverboard"],
        ["🏍 Motorcycle"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "እንኳን ወደ Hulu Gebeya በደህና መጡ!\n\nየሚፈልጉትን ምድብ ይምረጡ:",
        reply_markup=reply_markup
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🛴 Scooter":
        await update.message.reply_text("Scooter ክፍል ተመርጧል")

    elif text == "🛹 Hoverboard":
        await update.message.reply_text("Hoverboard ክፍል ተመርጧል")

    elif text == "🏍 Motorcycle":
        await update.message.reply_text("Motorcycle ክፍል ተመርጧል")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))

    app.run_polling()

if name == "__main__":
    main()
