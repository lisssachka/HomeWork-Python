from random import randint
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from bot_commands import *
DEFAULT_CANDIES = 120
MAX_CANDIES = 28

candies = DEFAULT_CANDIES
is_bot = False

def smart_bot(candies_out, player_candies, max_candies = 28):
    if candies_out - max_candies < 1:
        return max_candies + (candies_out - max_candies)

    if candies_out - player_candies > max_candies:
        return player_candies

    if candies_out <= max_candies * 2:
        res_value = candies_out - (max_candies + 1)
        return res_value if res_value else max_candies

    return max_candies


def check_candies(candies_out, took_candies, chat_id, context, max_candies = 28):
    if (took_candies > max_candies) or (took_candies < 1):
        tg_out(f'Конфеты можно брать только в диапазоне [1-{max_candies}]!',
               chat_id,context)
        return False

    if took_candies > candies_out:
        tg_out('На столе осталось меньше конфет!',
               chat_id, context)
        return False

    return True


