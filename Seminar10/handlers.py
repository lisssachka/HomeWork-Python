from telegram import Update
from telegram.ext import (CommandHandler,
                          MessageHandler,
                          Filters,
                          CallbackContext,
                          ConversationHandler)

from calculator import process_func
from logger import log


STATES = (0, 1)

def start(update: Update, context: CallbackContext) -> int:
    context.bot.send_message(update.effective_chat.id,
                             'Привет, я бот-калькулятор!')
    context.bot.send_message(update.effective_chat.id,
                             'Введите выражение без скобок и отрицательных чисел\nНапример: 2+3*6')
    return STATES[1]

def calculator(update: Update, context: CallbackContext) -> int:
    user_id = update.effective_user.id
    username = update.effective_user.username
    if username:
        username = '@' + username

    msg_data = update.message.text

    result = str(process_func(msg_data))

    context.bot.send_message(update.effective_chat.id, f'Результат: {result}')

    log(user_id, username, msg_data, result)

    return STATES[1]

def repeat(update: Update, context: CallbackContext) -> int:
    context.bot.send_message(update.effective_chat.id,
                             'Введите выражение без скобок и отрицательных чисел\nНапример: 2+3*6')
                           
def cancel(update: Update, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, 'Пока!!!')

start_handler = CommandHandler('start', start)
calculator_handler = MessageHandler(Filters.text, calculator)
cancel_handler = CommandHandler('cancel', cancel)

conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={
                                       STATES[0]: [start_handler],
                                       STATES[1]: [calculator_handler],
                                   },
                                   fallbacks=[cancel_handler])