import requests
from dotenv import dotenv_values
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler

config = dotenv_values(".env")


logging.basicConfig(
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level=logging.INFO
)


async def get_apy():
    apy_req = requests.get(config["APIURL"]).json()
    apy = (float(apy_req['data'][0]['avgApr']) * 100)
    return apy


async def apy(update: Update, context: CallbackContext.DEFAULT_TYPE):
    apy = await get_apy()
    await context.bot.send_message(chat_id=update.effective_chat.id, text="FlexUSD AvgAPY: {}%".format(apy))


if __name__ == '__main__':
    application = ApplicationBuilder().token(config['TGTOKEN']).build()
    apy_handler = CommandHandler('apy', apy)
    application.add_handler(apy_handler)
    application.run_polling()