from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Xin chào! Tôi là bot Telegram.")

app = ApplicationBuilder().token("8039028794:AAHP9naaK2Th0g8LY2-In2c7K20-nDzQVFI").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
