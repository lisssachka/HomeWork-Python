# from os import getenv

# from telegram import Bot, Update
# (Updater, CommandHandler, MessageHandler,Filters, CallbackContext, ConversationHandler)
from telegram.ext import ConversationHandler
from model import *
STATES = (0, 1)
DEFAULT_CANDIES = 120
MAX_CANDIES = 28

def start(update, context):
    tg_out('Привет\nЯ бот для игры в конфеты',
           update.effective_chat.id, context)
    tg_out(f'На столе 120 конфет',
           update.effective_chat.id, context)
    tg_out(f'Введите количество конфет [1-28]',
           update.effective_chat.id, context)
    return STATES[0]

def tg_out(text, chat_id, context):
    context.bot.send_message(chat_id, text)

def restart_game(update, context):
    global candies

    candies = DEFAULT_CANDIES
    decision = update.message.text

    if decision.lower() not in ('да', 'y', 'yes'):
        tg_out('Спасибо за игру!', update.effective_chat.id, context)
        return ConversationHandler.END

    tg_out('Перезапуск игры...', update.effective_chat.id, context)
    tg_out(f'На столе {candies} конфет',
           update.effective_chat.id, context)
    tg_out(f'Введите количество конфет (1-{MAX_CANDIES})',
           update.effective_chat.id, context)
    return STATES[0]


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'До свидания!')

def game(update, context):
    global candies, is_bot

    candies_limit = MAX_CANDIES if candies >= MAX_CANDIES else candies

    took_candies = int(update.message.text)

    if not check_candies(candies, took_candies,
                         update.effective_chat.id,
                         context, candies_limit):
        tg_out(f'Введите количество конфет [1-{candies_limit}]',
               update.effective_chat.id, context)

        return STATES[0]

    is_bot = False
    candies -= took_candies

    tg_out(f'Вы взяли {took_candies} конфет, осталось {candies}',
           update.effective_chat.id, context)

    if candies:
        is_bot = True

        took_candies = smart_bot(candies, took_candies, candies_limit)
        candies -= took_candies

        tg_out(f'Я взял {took_candies} конфет, осталось {candies}',
               update.effective_chat.id, context)

    if not candies:
        tg_out(['Вы выиграли!', 'Выиграл я!'][is_bot],
               update.effective_chat.id, context)
        tg_out('Хотите снова сыграть?\nВведите "да", "y" или "yes"',
               update.effective_chat.id, context)

        return STATES[1]

    tg_out(f'Введите количество конфет [1-{candies_limit}]',
               update.effective_chat.id, context)

    return STATES[0]