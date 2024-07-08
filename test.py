from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
SOLD45 = ('Sold is SoldAc = 100$')
# Your bot token
BOT_TOKEN = '6338220500:AAHzsnKASQY5YM9K7Ei-qEVPZRzZhXYPxWk'
# Your chat ID
AUTHORIZED_CHAT_ID = 6795721035

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! Send /sold to get the sold information.')

async def sold(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    if chat_id == AUTHORIZED_CHAT_ID:
        await update.message.reply_text(SOLD45)
    else:
        await update.message.reply_text('You are not authorized to use this command.')

def main() -> None:
    # Create the Application and pass it your bot's token.
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register the command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("sold", sold))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()

