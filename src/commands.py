from telegram import Update
from telegram.ext import CallbackContext
from helpers import get_apy

async def apy(update: Update, context: CallbackContext.DEFAULT_TYPE):
    apy = await get_apy()
    await context.bot.send_message(chat_id=update.effective_chat.id, text="FlexUSD AvgAPY: {}%".format(apy))