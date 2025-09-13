# main.py - Entry point for the Telegram bot

import logging
from telegram.ext import Updater, CommandHandler
import signal_generator
import config

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    """Start command handler."""
    update.message.reply_text('Simple Trading Bot ready! Use /signal for trade signals on multiple pairs.')

def signal_command(update, context):
    """Signal command handler."""
    signals = signal_generator.generate_signals()
    update.message.reply_text(signals)

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
