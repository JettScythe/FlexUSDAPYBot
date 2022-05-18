from dotenv import dotenv_values
import logging
from helpers import reformat_list_from_env, get_apy
from telegram.ext import CallbackContext

config = dotenv_values(".env")
async def broadcast(context: CallbackContext):
    apy = await get_apy()
    for chat_id in reformat_list_from_env(config["CHATIDS"]):
        await context.bot.send_message(chat_id=chat_id, text="FlexUSD AvgAPY: {}%".format(apy))
        logging.info("Sent message to {}".format(chat_id))    
