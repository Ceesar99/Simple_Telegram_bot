# main.py - Entry point for the Telegram bot

import logging
from telegram.ext import Updater, CommandHandler
import signal_generator
import config

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    """Start command handler."""
    update.message.reply_text('Simple Trading Bot ready! Use /signal for a trade signal.')

def signal_command(update, context):
    """Signal command handler."""
    df = signal_generator.fetch_data()
    signal = signal_generator.generate_signal(df)
    update.message.reply_text(signal)

def main():
    """Run the bot."""
    updater = Updater(config.TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('signal', signal_command))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
