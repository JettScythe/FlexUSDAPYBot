from dotenv import dotenv_values
import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from commands import apy
from jobs import broadcast

config = dotenv_values(".env")

logging.basicConfig(
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(config['TGTOKEN']).build()
    job_queue = application.job_queue
    apy_handler = CommandHandler('apy', apy)
    application.add_handler(apy_handler)
    broadcat_job = job_queue.run_repeating(broadcast, interval=43200, first=10)
    application.run_polling()